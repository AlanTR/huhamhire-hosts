# coding: gbk
"""
�ϲ�hostsģ���ļ�
"""
import os, shutil

class combineHosts:
    def __init__(self, dir):
        #����·��
        self.dir = dir
        self.IPvX = ['ipv4', 'ipv6']
        #����ģ��
        self.coremods = ['google', 'youtube', 'facebook', 'twitter', 'wikipedia', 'other']
        self.sharemods = ['activation', 'apple']
        self.coredir = '_mods/'
        self.sharedir = 'share_mods/'
        #��ģ��
        self.modules = ['info', 'timestamp', 'localhost']
        #�������ģ��
        self.admods = ['hostsx','mwsl', 'yoyo', 'mvps']
        self.adfile = 'adblock'
        self.adsubdir = 'adblock_mods/'        
        #��չ������
        self.fileext = '.hosts'
        
        #������ʱ·��
        self.tmpdir = 'tmp/'
        try:
            os.makedirs(dir + self.tmpdir)
        except WindowsError:
            pass
        
    def combineCore(self, ip):
        #�ϲ������б�
        
        #�趨ģ��
        mods = []
        mods.append(self.sharedir + self.sharemods[0])
        for mod in self.coremods:
            mods.append(ip + self.coredir + mod)
        mods.append(self.sharedir + self.sharemods[1])
        
        self.corefile = self.tmpdir + 'core_' + ip
        outstream = open(self.dir + self.corefile + self.fileext, 'w')
        
        #�ϲ�����
        for module in mods:
            instream = open(self.dir + module + self.fileext, 'r')
            lines = instream.readlines()
            for line in lines:
                outstream.write(line)
            instream.close()
            outstream.write('\n')
        outstream.close()
        
    def combineMain(self, ip):
        #�ϲ����б�
        self.outfile = self.tmpdir + 'main_' + ip
        self.corefile = self.tmpdir + 'core_' + ip
        outstream = open(self.dir + self.outfile + self.fileext, 'w')
        mods = self.modules
        mods.append(self.corefile)
        for module in mods:
            instream = open(self.dir + module + self.fileext, 'r')
            lines = instream.readlines()
            for line in lines:
                outstream.write(line)
            instream.close()
            outstream.write('\n')
        outstream.close()
        
        mods.remove(self.corefile)                                      #ɾ������ģ��
        os.remove(self.dir + self.corefile + self.fileext)              #ɾ�������ļ�
    
    def combineAdblock(self):
        #�ϲ���������б�
        outstream = open(self.dir + self.tmpdir + self.adfile + self.fileext, 'w')
        outstream.write('# region adblock\n\n')
        mods = self.admods
        for module in mods:
            instream = open(self.dir + self.adsubdir + module + self.fileext, 'r')
            lines = instream.readlines()
            for line in lines:
                outstream.write(line)
            instream.close()
            outstream.write('\n')
        outstream.write('# endregion')
        outstream.close()
    
    def run(self):
        #ִ�����
        for cate in self.IPvX:
            self.combineCore(cate)          #�ϲ������ļ�
            self.combineMain(cate)          #�ϲ����ļ�
        self.combineAdblock()
    
    def delTmpDir(self):
        #ɾ����ʱĿ¼
        shutil.rmtree(self.dir + self.tmpdir)
        
if __name__ == '__main__':
    ops = combineHosts('./')
    ops.run()
    print('Done!')\