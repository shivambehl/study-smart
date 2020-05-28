import random
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import wordnet as wn
from scripts.clean import *


class Text:
    def __init__(self, text):
        self.text = text
        self.tokenized_text = clean_text(text)
        self.sents = sent_tokenize(text)
        self.fdist = None
        self.senetence_pos_dic = None

    def get_top_words(self, k=5):
        '''
        returns list of tupples
        '''
        words = give_all_words(self.tokenized_text)
        fdist = FreqDist(words)
        self.fdist = fdist
        return fdist.most_common(k)

    def get_vocab(self):
        return len(set(self.tokenized_text))

    def get_lexical_richness(self):
        return len(set(self.tokenized_text)) / len(self.tokenized_text)

    def average_word_length(self):
        word_lengths = [len(words) for words in self.tokenized_text]
        return sum(word_lengths) / len(self.tokenized_text)

    def pos(self):
        taged_sents = []
        for sent in self.sents:
            sent = tokenizer.tokenize(sent)
            taged_sents.append(nltk.pos_tag(sent))
        return taged_sents

    def get_sentence_pos_dictionary(self):
        senetence_pos_dic = {}
        for sent in self.sents:
            token_sent = tokenizer.tokenize(sent)
            taged_sent = nltk.pos_tag(token_sent)
            pos_dic = {}
            senetence_pos_dic[sent] = pos_dic
            for s in taged_sent:
                word = s[0]
                pos_tag = s[1]
                # print(pos_tag)
                if pos_tag not in pos_dic:
                    # initialise pos_dic as an empty list
                    pos_dic[pos_tag] = []
                pos_dic[pos_tag].append(s[0])
        return senetence_pos_dic

    def generate_questions(self):
        questions = []
        senetence_pos_dic = self.get_sentence_pos_dictionary()
        for sent in self.sents:
            dic = senetence_pos_dic[sent]
            selected_words = []
            if 'NNP' in dic:
                selected_words = dic['NNP']
            elif 'NP' in dic:
                selected_words = dic['NP']

            if len(selected_words) > 0:
                ans = random.choice(selected_words)
                blank = '__' * len(ans)
                blank_sentence_maker = re.compile(re.escape(ans), re.IGNORECASE)
                blanked_sentence = blank_sentence_maker.sub(blank, sent)
            else:
                continue

            options = self.get_options(ans)

            if options is None:
                continue

            new_question = Que(blanked_sentence, ans, options)

            questions.append(new_question)

        return questions

    def get_options(self, word, n=4):
        """
        Using wordnet to get synonyms

        INPUT - target word

        OUTPUT - Function returns a list of n+1 words,
                n wrong and 1 right answer to the question
        """

        try:
            synset = wn.synsets(word, pos='n')[0]
        except:
            return None

        try:
            hypernym = synset.hypernyms()[0]
        except:
            return None
        hyponyms = hypernym.hyponyms()

        synonyms = []  # the list of synonymns

        for hyponym in hyponyms:
            option = hyponym.lemmas()[0].name().replace('_', ' ')
            # print(similar_word)
            if option != word:
                synonyms.append(option)

            if len(synonyms) >= 100:
                break

        if len(synonyms) >= n:
            options = random.choices(synonyms, k=n)
            options.append(word)
        else:
            options = None

        return options


class Que:
    def __init__(self, blanked_sentence, ans, options):
        self.question = blanked_sentence
        self.ans = ans
        random.shuffle(options)
        self.options = options
