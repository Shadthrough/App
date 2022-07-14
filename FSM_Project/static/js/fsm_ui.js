var fsm = (function() {
	var self = null;
	var delegate = null;
	var container = null;
	var stateCounter = 0;
	var saveLoadDialog = null;
	var alias = {};

	var localStorageAvailable = function () {
		return (typeof Storage !== "undefined"  && typeof localStorage !== "undefined");
	};

	var refreshLocalStorageInfo = function() {
		if (localStorageAvailable()) {
			$('#storedMachines').empty();
			var keys = [];
			for (var i=0; i < localStorage.length; ++i) {
				keys.push(localStorage.key(i));
			}
			keys.sort();
			$.each(keys, function(idx, key) {
				$('<li></li>', {'class':'machineName'})
					.append($('<span></span>').html(key))
					.append('<div class="delete" style="display:none;" title="Delete"><img class="delete" src="images/empty.png" /></div>')
					.appendTo('#storedMachines');
			});
		}
	};

	var makeSaveLoadDialog = function() {
		saveLoadDialog = $('#saveLoadDialog');
		$('#saveLoadTabs').tabs();
		$('#saveLoadTabs textarea').height(275);
		if (!localStorageAvailable()) {
			$('#saveLoadTabs')
				.tabs('option', 'active', 1)
				.tabs('option', 'disabled', [0])
				.find('ul li').eq(0).attr('title', 'Browser Storage not supported in this browser');
		}
		saveLoadDialog.dialog({
			autoOpen: false,
			dialogClass: 'loadSave no-close',
			width: 500,
			height: 450,
			open: function() {
				saveLoadDialog.find("div.ui-tabs-panel:not(.ui-tabs-hide)").find('input, textarea').focus();

			}
		});

		// Event Handlers for the LocalStorage widget
		$('#machineName').focus(function() {if ($(this).val() === $(this).attr('title')) {$(this).val('');}})
			.blur(function() {if($(this).val() === '') {$(this).val($(this).attr('title'));}})
			.keyup(function(event) {
				if (event.which === $.ui.keyCode.ENTER) {
					saveLoadDialog.parent().find('.ui-dialog-buttonpane button').eq(-1).trigger('click');
			}});

		$('#storedMachines').on('mouseover', 'li.machineName', function(event) {
			$(this).find('div.delete').show();
		}).on('mouseout', 'li.machineName', function(event) {
			$(this).find('div.delete').hide();
		}).on('click', 'li.machineName div.delete', function(event) {
			event.stopPropagation();
			localStorage.removeItem($(this).closest('li.machineName').find('span').html());
			refreshLocalStorageInfo();
		}).on('click', 'li.machineName', function(event) { // select the machineName
			$('#machineName').val($(this).find('span').html()).focus();
		}).on('dblclick', 'li.machineName', function(event) {	// immediately load the machineName
			$('#machineName').val($(this).find('span').html());
			saveLoadDialog.parent().find('.ui-dialog-buttonpane button').eq(-1).trigger('click');
		});
	};

	var initJsPlumb = function() {
		jsPlumb.importDefaults({
			Anchors: ["Continuous", "Continuous"],
			ConnectorZIndex: 5,
			ConnectionsDetachable: false,
			Endpoint: ["Dot", {radius:2}],
			HoverPaintStyle: {strokeStyle:"#d44", lineWidth:2},
			ConnectionOverlays: [
				["Arrow", {
					location: 1,
					length: 14,
					foldback: 0.8
					}],
				["Label", {location:0.5}]
			],
			Connector: ["StateMachine", {curviness:20}],
			PaintStyle: {strokeStyle:'#000', lineWidth:2}
		});

		jsPlumb.bind("click", connectionClicked);
	};

	var initStateEvents = function() {
		// Setup handling the 'delete' divs on states
		container.on('mouseover', 'div.state', function(event) {
			$(this).find('div.delete').show();
		}).on('mouseout', 'div.state', function(event) {
			$(this).find('div.delete').hide();
		});
		container.on('click', 'img.delete', function(event) {
			self.removeState($(this).closest('div.state'));
		});
		container.on('click', 'span.stateName', function(event) {
			self.renameState($(this).closest('div.state'));
		})

		// Setup handling for accept state changes
		container.on('change', 'input[type="checkbox"].isAccept', function(event) {
			var cBox = $(this);
			var stateId = cBox.closest('div.state').attr('id');
			if (cBox.prop('checked')) {
				delegate.fsm().addAcceptState(stateId);
				document.getElementById(stateId).style.border = 'thick double #55a';
			} else {
				delegate.fsm().removeAcceptState(stateId);
				document.getElementById(stateId).style.border = 'solid 2px #555555';
			}
		});
	};

	var initFSMSelectors = function() {
		// Setup the Automaton type listeners:
		$('button.delegate').on('click', function() {
			var newDelegate = null;
			switch ($(this).html()) {
				case 'DFA': newDelegate = dfa_delegate; break;
				case 'NFA': newDelegate = nfa_delegate; break;
				case 'PDA': newDelegate = pda_delegate; break;
			}
			if (newDelegate !== delegate) {
				self.setDelegate(newDelegate);
				$('button.delegate').prop('disabled', false);
				$(this).prop('disabled', true);
			}
		});

		$('button.delegate').each(function() {
			if ($(this).html() === 'DFA') { // Default to DFA
				$(this).click();
			}
		});
	};

	var loadSerializedFSM = function(serializedFSM) {
		var model = serializedFSM;
		if (typeof serializedFSM === 'string') {
			model = JSON.parse(serializedFSM);
		}

		// Load the delegate && reset everything
		self.reset();
		$('button.delegate').each(function() {
			if ($(this).html() === model.type) {
				$(this).click();
			}
		});

		// Load Bulk Tests
		// $('#acceptStrings').val(model.bulkTests.accept);
		// $('#rejectStrings').val(model.bulkTests.reject);

		// Create states
		$.each(model.states, function(stateId, data) {
			var state = null;
			if (stateId !== 'start') {
				state = makeState(stateId, data.displayId)
					.css('left', data.left + 'px')
					.css('top', data.top + 'px')
					.appendTo(container);
				jsPlumb.draggable(state, {containment:"parent"});
				makeStatePlumbing(state);
			} else {
				state = $('#start');
			}
			if (data.isAccept) {
				state.find('input.isAccept').prop('checked', true);
				document.getElementById(state.attr('id')).style.border = 'thick double #55a';
			} //---------------------------------------------------
		});

		// Create Transitions
		jsPlumb.unbind("jsPlumbConnection"); // unbind listener to prevent transition prompts
		$.each(model.transitions, function(index, transition) {
			jsPlumb.connect({source:transition.stateA, target:transition.stateB}).setLabel(transition.label);
		});
		jsPlumb.bind("jsPlumbConnection", delegate.connectionAdded);

		// Deserialize to the fsm
		delegate.deserialize(model);
	};

	var updateStatusUI = function(status) {
		$('#fsmDebugInputStatus span.consumedInput').html(status.input.substring(0, status.inputIndex));
		if (status.nextChar === '') {
			$('#fsmDebugInputStatus span.currentInput').html(delegate.getEmptyLabel());
			$('#fsmDebugInputStatus span.futureInput').html(status.input.substring(status.inputIndex));
		} else if (status.nextChar === null) {
			$('#fsmDebugInputStatus span.currentInput').html('[End of Input]');
			$('#fsmDebugInputStatus span.futureInput').html('');
		} else {
			$('#fsmDebugInputStatus span.currentInput').html(status.input.substr(status.inputIndex, 1));
			$('#fsmDebugInputStatus span.futureInput').html(status.input.substring(status.inputIndex+1));
		}

	};

	var connectionClicked = function(connection) {
		delegate.connectionClicked(connection);
	};

	var checkHashForModel = function() {
		var hash = window.location.hash;
		hash = hash.replace('#', '');
		hash = decodeURIComponent(hash);
		if (hash) {loadSerializedFSM(hash);}
	};

	var domReadyInit = function() {
		self.setGraphContainer($('#machineGraph'));

		$(window).resize(function() {
			container.height($(window).height() - $('#mainHolder h1').outerHeight() - $('#footer').outerHeight() - $('#bulkResultHeader').outerHeight() - $('#resultConsole').outerHeight() - 30 + 'px');
			jsPlumb.repaintEverything();
		});
		$(window).resize();

		// Setup handling 'enter' in test string box
		$('#testString').keyup(function(event) {if (event.which === $.ui.keyCode.ENTER) {$('#testBtn').trigger('click');}});

		container.dblclick(function(event) {
			self.addState({top: event.offsetY, left: event.offsetX});
		});

		initJsPlumb();
		initStateEvents();
		initFSMSelectors();
		makeSaveLoadDialog();

		var exampleBox = $('#examples').on('change', function() {
			if ($(this).val() !== '') {
				loadSerializedFSM(fsm_examples[$(this).val()]);
				$(this).val('');
			}
		});
		$.each(fsm_examples, function(key, serializedFSM) {
			$('<option></option>', {value:key}).html(key).appendTo(exampleBox);
		});

		checkHashForModel();
	};

	var makeStartState = function() {
		var startState = makeState('start');
		startState.find('div.delete').remove(); // Can't delete start state
		container.append(startState);
		makeStatePlumbing(startState);
	};

	/**
	 * Create a new state.
	 * @param {string} stateId Internal ID of the new state.
	 * @param {string} [displayId] Displayed ID of the state, by default the internal ID.
	 */
	var makeState = function(stateId, displayId) {
		displayId = displayId || stateId;
		return $('<div id="' + stateId + '" class="state" data-displayid="' + displayId + '"></div>')
			.append('<input id="' + stateId+'_isAccept' + '" type="checkbox" class="isAccept" value="true" title="Accept State" />')
			.append('<span class="stateName">' + displayId + '</span>')
			.append('<div class="plumbSource" title="Drag from here to create new transition">&nbsp;</div>')
			.append('<div class="delete" style="display:none;"><img class="delete" src="../../static/images/empty.png"  title="Delete"/></div>');
	};

	var makeStatePlumbing = function(state) {
		var source = state.find('.plumbSource');
		jsPlumb.makeSource(source, {
			parent: state,
			maxConnections: 10,
			onMaxConnections:function(info, e) {
				alert("Maximum connections (" + info.maxConnections + ") reached");
			},
		});

		jsPlumb.makeTarget(state, {
			dropOptions: {hoverClass:'dragHover'}
		});
		return state;
	};
	
	return {

		tmpTest : function () {
			// $('#resultConsole').empty();
			var serializedModel = delegate.serialize();
			// var grammar = new File('fsm.g');
			var line = 'grammar fsm;\n@parser::members {\npaths = []\n}\n'; //backtrack=true\; {parser.paths.append('${path}->')} @parser::members {\nself.paths = []\n}\n
			var checked = [];
			console.log(serializedModel)
			var trans = serializedModel.dfa.transitions;
			console.log(Object.keys(serializedModel.states));
			var pass = true;
			var dead = [];
			line = line + `expr: start;\n`
			Object.keys(trans).forEach(key => {
				line = line + `${key} : `;
				var paths = Object.keys(trans[key])
				paths.forEach(path => {
					if (pass){
						line = line + `'#' ${key}\n| `;
						pass = false;
					}
					if (checked.includes(trans[key][path])){
						console.log('');
					}
					else{
						line = line + `'#' ${trans[key][path]} {self.paths.append('-${path}>${trans[key][path]}')}\n| `; //{self.paths.append('-${path}>${trans[key][path]}')}
						checked.push(trans[key][path]);
						// console.log(checked);
					}
					if (serializedModel.dfa.acceptStates.includes(key)) {
						line = line + `EOF\n| `;
					}
					if (paths[paths.length-1] != path){
						line = line + `'${path}' ${trans[key][path]} {self.paths.append('-${path}>${trans[key][path]}')}\n| `; //{self.paths.append('-${path}>${trans[key][path]}')}
					}
					else{
						line = line + `'${path}' ${trans[key][path]} {self.paths.append('-${path}>${trans[key][path]}')}`; //{self.paths.append('-${path}>${trans[key][path]}')}
					}
					if (!Object.keys(serializedModel.dfa.transitions).includes(trans[key][path])){
						dead.push(trans[key][path]);
					}
				});
				pass = true;
				checked = [];
				line = line + `\n\;\n`;
			});
			dead.forEach(state => {
				line = line + `${state} : '#' ${state}`;
				if (serializedModel.dfa.acceptStates.includes(state)) {
					line = line + `\n| EOF\n`;
				}
				line = line + `\;\n`;
				});
			var data = {
				'grammar' : line,
				'input' : $('#testString').val(),
				'states': Object.keys(serializedModel.states).length
			};
			$.post("antlr", data=data, function (res) {
				res = res.split('|');
				console.log(res[0])
				var accepts = res[0] === 'Accepted' ? true : false;
				$('#testResult').html(accepts ? 'Accepted' : 'Rejected').effect('highlight', {color: accepts ? '#bfb' : '#fbb'}, 2000);
				
				$('<div></div>', {'class':'', 'style':(accepts ? 'background-color: lightgreen;' : 'background-color: tomato;') + 'width: 100%; display: block; padding: 2px;'}).append(data.input + ' -- ' + res[0] + '\t' + res[1]).appendTo('#resultConsole');
				
				$(res[1]).appendTo('#resultConsole');
			});
		},

		init: function() {
			self = this;
			$(domReadyInit);
			return self;
		},

		setDelegate: function(newDelegate) {
			delegate = newDelegate;
			delegate.setContainer(container);
			delegate.reset().fsm().setStartState('start');
			jsPlumb.unbind("jsPlumbConnection");
			jsPlumb.reset();
			container.empty();
			initJsPlumb();
			jsPlumb.bind("jsPlumbConnection", delegate.connectionAdded);
			stateCounter = 0;
			makeStartState();
			return self;
		},

		setGraphContainer: function(newContainer) {
			container = newContainer;
			jsPlumb.Defaults.Container = container;
			return self;
		},

		addState: function(location) {
			while ($('#s'+stateCounter).length > 0) {++stateCounter;} // Prevent duplicate states after loading
			var state = makeState('s' + stateCounter);
			if (location && location.left && location.top) {
				state.css('left', location.left + 'px')
				.css('top', location.top + 'px');
			}
			container.append(state);
			jsPlumb.draggable(state, {containment:"parent"});
			makeStatePlumbing(state);
			// Do nothing to model
			return self;
		},

		/**
		 * Change the displayed name of a state. The start state cannot
		 * be renamed, it’s a no-op if the given state is the start state.
		 * @param {jQuery} state The state to rename.
		 */
		renameState: function(state) {
			if (state.attr('id') !== 'start') {
				var newname = window.prompt('New name', state.data('displayid'));
				if (newname) {
					if (newname.length > 6) {
						// switchNote
					}
					else{
						state.data('displayid', newname);
						state.find('.stateName').text(newname);
					}
				}
			}
		},

		removeState: function(state) {
			var stateId = state.attr('id');
			jsPlumb.select({source:stateId}).detach(); // Remove all connections from UI
			jsPlumb.select({target:stateId}).detach();
			state.remove(); // Remove state from UI
			delegate.fsm().removeTransitions(stateId); // Remove all transitions from model touching this state
			delegate.fsm().removeAcceptState(stateId); // Assure no trace is left
			return self;
		},

		removeConnection: function(connection) {
			jsPlumb.detach(connection);
		},

		test: function(input) {
			if ($.type(input) === 'string') {
				$('#testResult').html('Testing...')
				var accepts = delegate.fsm().accepts(input);
				$('#testResult').html(accepts ? 'Accepted' : 'Rejected').effect('highlight', {color: accepts ? '#bfb' : '#fbb'}, 1000);
			} else {
				$('#resultConsole').empty();
				var makePendingEntry = function(input, type) {
						return $('<div></div>', {'class':'pending', title:'Pending'}).append(type + ': ' + (input === '' ? '[Empty String]' : input)).appendTo('#resultConsole');
				};
				var updateEntry = function(result, entry) {
					entry.removeClass('pending').addClass(result).attr('title', result).append(' -- ' + result);
				};
				$.each(input.accept, function(index, string) {
					updateEntry((delegate.fsm().accepts(string) ? 'Pass' : 'Fail'), makePendingEntry(string, 'Accept'));
				});
				$.each(input.reject, function(index, string) {
					updateEntry((delegate.fsm().accepts(string) ? 'Fail' : 'Pass'), makePendingEntry(string, 'Reject'));
				});
				$('#bulkResultHeader').effect('highlight', {color: '#add'}, 1000);
			}
			return self;
		},

		debug: function(input) {
			if ($('#stopBtn').prop('disabled')) {
				$('#testResult').html('&nbsp;');
				$('#stopBtn').prop('disabled', false);
				$('#stopBtn').css('background-color', '#680000;');
				$('#debugBtn').css('background-color', '#058800;');
				$('#loadBtn, #testBtn, #bulkTestBtn, #testString, #resetBtn').prop('disabled', true);
				$('button.delegate').prop('disabled', true);
				$('#fsmDebugInputStatus').show();
				delegate.debugStart();
				delegate.fsm().stepInit(input);
			} else {
				delegate.fsm().step();
			}
			var status = delegate.fsm().status();
			updateStatusUI(status);
			delegate.updateUI();
			if (status.status !== 'Active') {
				$('#testResult').html(status.status === 'Accept' ? 'Accepted' : 'Rejected').effect('highlight', {color: status.status === 'Accept' ? '#bfb' : '#fbb'}, 1000);
				$('#debugBtn').prop('disabled', true);
			}
			return self;
		},

		debugStop: function() {
			$('#fsmDebugInputStatus').hide();
			$('#stopBtn').prop('disabled', true);
			$('#stopBtn').css('background-color', '#555555;');
			$('#debugBtn').css('background-color', '#555555;');
			$('#loadBtn, #testBtn, #bulkTestBtn, #debugBtn, #testString, #resetBtn').prop('disabled', false);
			$('button.delegate').prop('disabled', false).each(function() {
				switch ($(this).html()) {
					case 'DFA': if (delegate === dfa_delegate) {$(this).prop('disabled', true);} break;
					case 'NFA': if (delegate === nfa_delegate) {$(this).prop('disabled', true);} break;
					case 'PDA': if (delegate === pda_delegate) {$(this).prop('disabled', true);} break;
				}
			});
			delegate.debugStop();
			return self;
		},

		reset: function() {
			self.setDelegate(delegate);
			$('#testString').val('');
			$('#testResult').html('&nbsp;');
			$('#acceptStrings').val('');
			$('#rejectStrings').val('');
			$('#resultConsole').empty();
			return self;
		},

		load: function() {
			$('#plaintext textarea').empty();
			$('#code textarea').empty();
			var finishLoading = function() {
				self.setDelegate(delegate);
				var serializedModel = null;
				if ($('#saveLoadTabs').tabs('option', 'active') === 0){
					serializedModel = saveLoadDialog.find('textarea').val();
				}
				else{
					inpCCode = saveLoadDialog.find('#code textarea').val();
					var model = delegate.serialize();
					console.log(model);
					if(inpCCode.indexOf('switch') === -1){
						alert('Конечный автомат не обнаружен в коде');
						return false;
					}
					else{
						var states = {};
						var transitions = new Object();
						var casePos = '';
						var curr_state;
						var trans_state;
						var curr_trans;
						var transs = []
						while (inpCCode.indexOf('case') !== -1) {
							inpCCode = inpCCode.slice(inpCCode.indexOf('case'));
							inpCCode = inpCCode.slice(inpCCode.indexOf('\'')+1);
							curr_state = (inpCCode.slice(0, inpCCode.indexOf('\'')));
							states[curr_state] = {};
							transitions[curr_state] = new Object;
							if(inpCCode.indexOf('if') !== -1){
								inpCCode = inpCCode.slice(inpCCode.indexOf('if'));
								inpCCode = inpCCode.slice(inpCCode.indexOf('\'')+1);
								curr_trans = (inpCCode.slice(0, inpCCode.indexOf('\'')));
								inpCCode = inpCCode.slice(inpCCode.indexOf('\'')+1);
								inpCCode = inpCCode.slice(inpCCode.indexOf('\'')+1);
								trans_state = (inpCCode.slice(0, inpCCode.indexOf('\'')));
								transitions[curr_state][curr_trans] = trans_state;
								transs.push(new Object({stateA: curr_state, label: curr_trans, stateB: trans_state}))							
							}
							casePos = inpCCode.slice(0, inpCCode.indexOf('break'));
							while(casePos.indexOf('else if') !== -1){
								inpCCode = inpCCode.slice(inpCCode.indexOf('if'));
								inpCCode = inpCCode.slice(inpCCode.indexOf('\'')+1);
								curr_trans = (inpCCode.slice(0, inpCCode.indexOf('\'')));
								inpCCode = inpCCode.slice(inpCCode.indexOf('\'')+1);
								inpCCode = inpCCode.slice(inpCCode.indexOf('\'')+1);
								trans_state = (inpCCode.slice(0, inpCCode.indexOf('\'')));
								transitions[curr_state][curr_trans] = trans_state;
								transs.push(new Object({stateA: curr_state, label: curr_trans, stateB: trans_state}))
								casePos = casePos.slice(casePos.indexOf('else if')+7);
							}
							inpCCode = inpCCode.slice(inpCCode.indexOf('break'));
						}
					}
					model.dfa.transitions = transitions;
					model.states = states;
					model.transitions = transs;
					console.log(model)
					serializedModel = JSON.stringify(model);
					console.log(serializedModel)
				}
				loadSerializedFSM(serializedModel);
				return true;
			};

			saveLoadDialog.dialog('option', {
				title: 'Конвертация из кода',
				buttons: {
					Cancel: function(){saveLoadDialog.dialog('close');},
					Load: function(){if (finishLoading()) {saveLoadDialog.dialog('close');}}
				}
			});
			$('#saveLoadTabs').off('tabsactivate');

			refreshLocalStorageInfo();
			$('#plaintext textarea').empty();
			$('#code textarea').empty();
			saveLoadDialog.dialog('open');
		},

		save: function() {
			var model = delegate.serialize();
			container.find('div.state').each(function() {
				var id = $(this).attr('id');
				if (id !== 'start') {
					$.extend(model.states[id], $(this).position());
					$.extend(model.states[id], {displayId: $(this).data('displayid')});
				}
			});
			model.bulkTests = {
				accept: $('#acceptStrings').val(),
				reject: $('#rejectStrings').val()
			};
			var serializedModel = JSON.stringify(model);
			console.log(model);
			///////////////////////////
			var c_code = `
			char str[100];
			printf("Введите строку для проверки: ");
			scanf("%s", str);
			int i;
			AcceptedStates = [${model.dfa.acceptStates}];
			char state[100] = '${model.dfa.startState}';
			for (i = 0; str[i] != '\\0'; i++)
			{
				switch (state)
				{`;
			var states_code = '';
			var i = 0;
			var transition_code = '';
			for (var cur_state in model.dfa.transitions)
			{
				states_code = states_code + `
				case '${cur_state}':
				`
				i = 0;
				transition_code = '';
				for (var cur_transaction in model.dfa.transitions[cur_state])
				{
					if (i == 0){
						transition_code = transition_code + `
						if (str[i] == '${cur_transaction}')
							state = '${model.dfa.transitions[cur_state][cur_transaction]}';
						break;`;
						i++;
					}
					else {
						transition_code = transition_code.slice(0, transition_code.length - 13);
						transition_code = transition_code + `
						else if (str[i] == '${cur_transaction}')
							state = '${model.dfa.transitions[cur_state][cur_transaction]}';
						break;`;
					}
				}
				states_code = states_code + transition_code;
			}

			c_code = c_code + states_code + `}
				}
		if (AcceptedStates.indexOf(state) !== -1)
			printf("String is accepted");
		else
			printf("String is not accepted");`;
			c_code = c_code.split('\t').join('');
			///////////////////////////
			// alert(c_code);
			var finishSaving = function() {
				var storageKey = $('#machineName').val();
				if (!storageKey) {alert("Please Provide a Name"); return false;}
				if (localStorageAvailable()) {
					localStorage.setItem(storageKey, serializedModel);
				} else {
					alert("Can't save machine to Browser Storage, this browser doesn't support it.");
					return false;
				}
				return true;
			};

			var buttonUpdater = function(event, ui) {
				if (ui.newPanel.attr('id') === 'browserStorage') {
					saveLoadDialog.dialog('option', 'buttons', {
						Cancel: function(){saveLoadDialog.dialog('close');},
						Save: function(){if (finishSaving()) {saveLoadDialog.dialog('close');}}
					});
				} else if (ui.newPanel.attr('id') === 'plaintext' || ui.newPanel.attr('id') === 'shareableURL') {
					ui.newPanel.find('textarea').select();
					saveLoadDialog.dialog('option', 'buttons', {
						Copy: function(){ui.newPanel.find('textarea').select();document.execCommand('copy')},
						Close: function(){saveLoadDialog.dialog('close');}
					});
				}
			};

			saveLoadDialog.dialog('option', 'title', 'Конвертация в код');
			$('#saveLoadTabs').on('tabsactivate', buttonUpdater);
			buttonUpdater(null, {newPanel: $('#saveLoadTabs div').eq($('#saveLoadTabs').tabs('option', 'active'))});

			refreshLocalStorageInfo();
			$('#plaintext textarea').val(serializedModel);
			$('#code textarea').val(c_code);///////////////////////////////////////////////////////////////////////
			$('#shareableURL textarea').val(window.location.href.split("#")[0] + '#' + encodeURIComponent(serializedModel));
			saveLoadDialog.dialog('open');
		}
	};
})().init();
