class CAnimal:
    def __init__(self,voice='hello'): # voice��ʼ��Ĭ��Ϊhello
        self.voice = voice
    def Say(self):
        print(self.voice)
    def Run(self):
        pass    # �ղ�����䣨�����κβ�����

class CDog(CAnimal):        		# �̳���CAnimal
    def SetVoice(self,voice): 		# �������Ӻ���SetVoice
        self.voice = voice
    def Run(self,voice): 			# �������غ���Run ����
        print('Running')

bobo = CDog()
bobo.SetVoice('My Name is BoBo!')
bobo.Say()
bobo.Run('lab')
#bobo.Run()