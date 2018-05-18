# -*- coding:utf-8 -*-


class CNode(object):
    def __init__(self):
        self.m_pPreCondition = None

    def SetPreCondition(self, pPreCondition):
        self.m_pPreCondition = pPreCondition

    def Enter(self):
        pass

    def Exit(self):
        pass

    def Execute(self):
        pass
