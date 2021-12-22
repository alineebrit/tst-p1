def unico (sequencia):

    aspas = ''
    if sequencia != aspas:
        aspas += sequencia[0]

        for i in range(1,len(sequencia)):
            if sequencia[i] != sequencia[i - 1]:
                aspas += sequencia[i]
    return (aspas)
