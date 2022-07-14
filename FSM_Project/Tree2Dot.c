for (i = 0; str[i] != '\0'; i++)
{
    switch (state)
    {
    case 'start':

        if (str[i] == 'L')
            state = 's0';
        else if (str[i] == 'S')
            state = 's4';
        break;
    case 's0':

        if (str[i] == 'C')
            state = 'start';
        else if (str[i] == 'K')
            state = 's2';
        else if (str[i] == 'S')
            state = 's4';
        break;
    case 's4':

        if (str[i] == 'C')
            state = 'start';
        else if (str[i] == 'K')
            state = 's2';
        else if (str[i] == 'D')
            state = 's1';
        break;
    case 's2':

        if (str[i] == 'R')
            state = 's0';
        else if (str[i] == 'A')
            state = 's1';
        else if (str[i] == 'L')
            state = 's5';
        break;
    case 's7':

        if (str[i] == 'U')
            state = 's9';
        break;
    case 's6':

        if (str[i] == 'A')
            state = 's10';
        break;
    case 's9':

        if (str[i] == 't')
            state = 's10';
        break;
    }
}
