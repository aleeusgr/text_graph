def txt_pipe(filename):

    '''
    Text feature generation.
    this module will load txt file from pwd 
    steps:
    1. Read text: 
    2. Lemmatization
    3. Stop words
    4. Bag of words
    5. di,3,4 grams.
    http://www.nltk.org/book/

    returns: lemmed: list, bag of words; grams: iterator object, 4-grams 

    '''
    with open('{}'.format(filename)) as fp:
        contents = fp.read()

    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import RegexpTokenizer
    
    stop_words = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer(r'\w+')
    #tokens = nltk.word_tokenize(contents)
    tokens = tokenizer.tokenize(contents)
    filtered_sentence = [w for w in tokens if not w in stop_words]
    
    tags = nltk.pos_tag(filtered_sentence)
    #stm = nltk.LancasterStemmer()
    #stm = nltk.PorterStemmer()
    wnl = nltk.WordNetLemmatizer()

    lemmed = [wnl.lemmatize(t[0]) for t in tags]
    grams = nltk.ngrams(lemmed,4)
    print(tags)
    # need to return POS tags too
    nodes = []
    for i in tags:
        nodes.append((i[0],{'POS':i[1]}))
    return nodes,grams

