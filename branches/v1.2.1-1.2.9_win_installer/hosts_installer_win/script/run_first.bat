@echo off
echo   ---------------------------------------------------------------------------
echo   ^| Vista/Win7 �û���ע�⣺                                                 ^|
echo   ^| Ϊ��֤��װ��ȷ����ִ�б��ļ�ʱ����"�Ҽ�"ѡ���ļ�-^>"�Թ���Ա�������"  ^|
echo   ---------------------------------------------------------------------------
pause
if not exist %SystemRoot%\System32\drivers\etc\hosts goto not_necessary
echo;
echo ����ɾ�������ļ�.....
del %SystemRoot%\System32\drivers\etc\hosts
if not exist %SystemRoot%\System32\drivers\etc\hosts goto success
echo ^^^����ʧ�ܣ���ȷ�������Թ���Ա������еı��ű�
echo;
goto end
:success
echo ^^������ɣ������˳������ִ�а�װ����
echo;
goto end
:not_necessary
echo;
echo ^hosts�ļ������ڣ�����ִ�б������������˳���ֱ��ִ�а�װ����
echo;
:end
pause