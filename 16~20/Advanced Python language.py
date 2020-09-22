'''
author: Wumo
Date: 20200917
'''

'''生成式（推导式）的用法'''
# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)


'''嵌套的列表的坑'''
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# # 录入五个学生三门课程的成绩
# # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# # scores = [[None] * len(courses)] * len(names)
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
#         print(scores)


"""
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""
# from abc import ABCMeta, abstractmethod
#
#
# class Employee(metaclass=ABCMeta):
#     """员工(抽象类)"""
#
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def get_salary(self):
#         """结算月薪(抽象方法)"""
#         pass
#
#
# class Manager(Employee):
#     """部门经理"""
#
#     def get_salary(self):
#         return 15000.0
#
#
# class Programmer(Employee):
#     """程序员"""
#
#     def __init__(self, name, working_hour=0):
#         self.working_hour = working_hour
#         super().__init__(name)
#
#     def get_salary(self):
#         return 200.0 * self.working_hour
#
#
# class Salesman(Employee):
#     """销售员"""
#
#     def __init__(self, name, sales=0.0):
#         self.sales = sales
#         super().__init__(name)
#
#     def get_salary(self):
#         return 1800.0 + self.sales * 0.05
#
#
# class EmployeeFactory:
#     """创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）"""
#
#     @staticmethod
#     def create(emp_type, *args, **kwargs):
#         """创建员工"""
#         all_emp_types = {'M': Manager, 'P': Programmer, 'S': Salesman}
#         cls = all_emp_types[emp_type.upper()]
#         # print(cls)
#         # print(cls(*args))
#         return cls(*args) if cls else None
#
#
# def main():
#     """主函数"""
#     emps = [
#         EmployeeFactory.create('M', '曹操'),
#         EmployeeFactory.create('P', '荀彧', 120),
#         EmployeeFactory.create('P', '郭嘉', 85),
#         EmployeeFactory.create('S', '典韦', 123000),
#     ]
#
#     for emp in emps:
#         print(f'{emp.name}: {emp.get_salary():.2f}元')
#
#
# if __name__ == '__main__':
#     main()



import random


# class Card(object):
#     """一张牌"""
#
#     def __init__(self, suite, face):
#         self._suite = suite
#         self._face = face
#
#     @property
#     def face(self):
#         return self._face
#
#     @property
#     def suite(self):
#         return self._suite
#
#     def __str__(self):
#         if self._face == 1:
#             face_str = 'A'
#         elif self._face == 11:
#             face_str = 'J'
#         elif self._face == 12:
#             face_str = 'Q'
#         elif self._face == 13:
#             face_str = 'K'
#         else:
#             face_str = str(self._face)
#         return '%s%s' % (self._suite, face_str)
#
#     def __repr__(self):
#         return self.__str__()
#
#
# class Poker(object):
#     """一副牌"""
#
#     def __init__(self):
#         # self._cards = []
#         # for face in range(1, 14):
#         #     for suite in '♠♥♣♦':
#         #         self._cards.append(Card(suite, face))
#         self._cards = [Card(suite, face)
#                        for suite in '♠♥♣♦'
#                        for face in range(1, 14)]
#         self._current = 0
#
#     @property
#     def cards(self):
#         return self._cards
#
#     def shuffle(self):
#         """洗牌(随机乱序)"""
#         self._current = 0
#         random.shuffle(self._cards)
#
#     @property
#     def next(self):
#         """发牌"""
#         card = self._cards[self._current]
#         self._current += 1
#         return card
#
#     @property
#     def has_next(self):
#         """还有没有牌"""
#         return self._current < len(self._cards)
#
#
# class Player(object):
#     """玩家"""
#
#     def __init__(self, name):
#         self._name = name
#         self._cards_on_hand = []
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def cards_on_hand(self):
#         return self._cards_on_hand
#
#     def get(self, card):
#         """摸牌"""
#         self._cards_on_hand.append(card)
#
#     def arrange(self, card_key):
#         """玩家整理手上的牌"""
#         self._cards_on_hand.sort(key=card_key)
#
#
# # 排序规则-先根据花色再根据点数排序
# def get_key(card):
#     return (card.suite, card.face)
#
#
# def main():
#     p = Poker()
#     p.shuffle()
#     players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
#     for _ in range(13):
#         for player in players:
#             player.get(p.next)
#     for player in players:
#         print(player.name + ':', end=' ')
#         player.arrange(get_key)
#         print(player.cards_on_hand)
#
#
# if __name__ == '__main__':
#     main()


"""
经验：符号常量总是优于字面常量，枚举类型是定义符号常量的最佳选择
"""
from enum import Enum, unique

import random


@unique
class Suite(Enum):
    """花色"""

    # SPADE, HEART, CLUB, DIAMOND = range(4)
    SPADE = 0
    HEART = 1
    CLUB = 2
    DIAMOND = 3

    print(SPADE)
    print(HEART)
    print(CLUB)
    print(DIAMOND)

    def __lt__(self, other):
        # print(self.value < other.value)
        return self.value < other.value


class Card():
    """牌"""

    def __init__(self, suite, face):
        """初始化方法"""
        self.suite = suite
        self.face = face

    def show(self):
        """显示牌面"""
        suites = ['♠', '♥', '♣', '♦']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __repr__(self):
        return self.show()


class Poker():
    """扑克"""

    def __init__(self):
        self.index = 0
        # self.cards = [Card(suite, face)
        #               for suite in Suite
        #               for face in range(1, 14)]

        self.cards = []
        for suite in Suite:
            # print(suite)
            for face in range(1, 14):
                self.cards.append(Card(suite, face))

    def shuffle(self):
        """洗牌（随机乱序）"""
        random.shuffle(self.cards)
        self.index = 0

    def deal(self):
        """发牌"""
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        return self.index < len(self.cards)


class Player():
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸一张牌"""
        self.cards.append(card)

    def absd(self,card):
        '''指定用什么来进行排序'''
        return card.suite, card.face

    '''
    def sort(self, comp=lambda card: (card.suite, card.face)):
    """整理手上的牌"""
    self.cards.sort(key=comp)
    '''
    def sort(self):
        """整理手上的牌"""
        print(self.cards)
        self.cards.sort(key=self.absd)

def main():
    """主函数"""
    poker = Poker()

    poker.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    while poker.has_more:
        for player in players:
            player.get_one(poker.deal())
    for player in players:
        player.sort()
        print(f'{player.name}的牌为:', end='')
        print(player.cards)



if __name__ == '__main__':
    main()
