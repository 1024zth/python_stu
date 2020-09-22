import random


class Card(object):
    """一张牌"""
    '''
    属性：花色，值
    '''

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)

    def __repr__(self):
        return self.__str__()


class Poker(object):
    """一副牌"""

    def __init__(self):
        # self._cards = []
        # for face in range(1, 14):
        #     for suite in '♠♥♣♦':
        #         self._cards.append(Card(suite, face))
        self._cards = [Card(suite, face)
                       for suite in '♠♥♣♦'
                       for face in range(1, 14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌(随机乱序)"""
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        '''判断是否有剩余牌'''
        return self._current < len(self._cards)


class Player(object):
    """玩家"""

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        """摸牌"""
        self._cards_on_hand.append(card)

    def arrange(self,card_key):
        '''整理牌'''
        self._cards_on_hand.sort(key=card_key)


# # 排序规则-先根据花色再根据点数排序
# def get_key(card):
#     return (card.suite, card.face)


def main():
    p = Poker()
    p.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    while p.has_next:
        for i in range(13):
            for player in players:
                player.get(p.next)
    for player in players:
        print(player.name + ':', end=' ')
        player.arrange(lambda card: (card.suite,card.face))
        print(player.cards_on_hand)
        # for _ in range(len(player.cards_on_hand)):
        #     current = 0
        #     print(player.cards_on_hand.pop(current), end=' ')
        #     current += 1
        # print('\n')
if __name__ == '__main__':
    main()