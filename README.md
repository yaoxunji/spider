doutuwang����ȥͼƬ
novelspider����ȡС˵�������߲����
Ȩ���Ժ����˲ο�

Scrapy�����

scrapy startproject name  ������Ŀ
scrapy genspider name1 [��ַ] ��������ģ��
scrapy crawl name1  ��������

scrapy shell ��ַ[����Ҫ����]
requset ��ַ��������Ӧ���󣬷��ص���Ӧ��Ϣ��shell�У�
view��response����������д�response�б������ҳ���ݣ�shell�У�
fetch��url�����·�������shell�У�

Scrapy��Ŀ�ļ�

init.py ->����Ĭ�ϣ��������
items.py ->�Զ�����Ŀ��ĵط��������ȡ����֮����ܵ��ļ�������
pipeline.py ->��Ŀ�ܵ��ļ����Դ������Ŀ���е����ݽ�����������
settings.py ->��Ŀ�������ļ������������ӳ٣���Ŀ�ܵ��ļ�����������Լ��Զ����м�������ú�˳��
middlewares.py ->�м�������ļ�
spiderĿ¼ ->����ֻ��һ��init.py�ļ�����ʹ��genspider֮���ࣩ���ڸ�Ŀ¼�¶��������ಢ�̳�

sqlite3���Ӳ�����database.py��
����һ���ѯ��ʱ��execute�������ᷴ�ؽ������ȡ�����Ҫ 
cu = conn.cursor #cursor�ǹ��
all_results = cu.fetchall()
fetchֻ��ִ��һ�Σ�fetch ����fetchone��fetchall��fetchmany��ָ������

