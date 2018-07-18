# -*- coding: utf-8 -*

from dateutil.relativedelta import relativedelta
from datetime import date

class config(object):
    #管理员在数据库里的 id
    admin_id = 1

    #Redis 数据库配置信息
    redis_addr = 'localhost'
    redir_port = 7012
    redis_password = ''
    redis_db = 0

    #数据库信息
    mysql_addr = 'localhost'
    mysql_port = 3306
    mysql_username = 'buubot_buump'
    mysql_password = ''
    mysql_database = 'buubot_buump'

    version = '20180626'

    #在外网，需要连入
    need_vpn = True

    #学期开始日期
    jwxt_first_week_monday = date(2018, 3, 12)

    #输出课表的依据，课程开始的时间
    jwxt_dict_week = {'一': 0, '二': 1, '三': 2, '四': 3, '五': 4, '六': 5, '日': 6}
    jwxt_dict_day = {
                    1: relativedelta(hours = 8, minutes = 00), 2: relativedelta(hours = 8, minutes = 50),
                    3: relativedelta(hours = 9, minutes = 55), 4: relativedelta(hours = 10, minutes = 45),
                    5: relativedelta(hours = 11, minutes = 35), 6: relativedelta(hours = 13, minutes = 00),
                    7: relativedelta(hours = 13, minutes = 50), 8: relativedelta(hours = 14, minutes = 50),
                    9: relativedelta(hours = 15, minutes = 40), 10: relativedelta(hours = 16, minutes = 40),
                    11: relativedelta(hours = 17, minutes = 30), 12: relativedelta(hours = 18, minutes = 20),
                    13: relativedelta(hours = 19, minutes = 10)
                }

    #aes 加密秘钥，随机字符串即可
    aes_key = ''

    #图灵机器人的key和公众号名称
    tuling_key = ''
    bot_nickname = '@联大小助'

    fail_clean = ['current_printer_id', 'operating', 'inputing', 'current_print_file_name', 'current_print_file_page_count' \
                    'current_print_file_print_price', 'current_print_create_time', 'current_page', 'total_page', 'word', 'operating']
    print_price = 0.2

    #smtp 配置
    smtp_server = 'smtp.mxhichina.com'
    smtp_username = 'printer@zhaoj.in'
    smtp_sender = 'printer@zhaoj.in'
    smtp_password = ''

    #微信公众号配置相关信息
    weixin_token = ''
    weixin_appid = ''
    weixin_appsecret = ''
    weixin_encoding_aeskey = ''

    #储存的配置，腾讯的 cos
    cos_app_id = '1251267611'
    cos_app_secret_id = ''
    cos_app_secret_key = ''
    cos_bucket_name = 'buurobot'
    cos_region = 'bj'
    cos_url = ''

    #公众号下面的按钮配置
    wechat_menu = {'button':[
        {
            'name': '关于小助',
            'sub_button': [
                {
                    'type': 'view',
                    'name': '意见反馈',
                    'url':  'https://jinshuju.net/f/w6qTir',
                },
                {
                    'type': 'media_id',
                    'name': '本号二维码',
                    'media_id': 'vAY3Fs9fVWi_MsFR8q0p-ovbjdtIDDNDKf_VTvcga1g',
                },
            ],
        }
    ]}

    #学校内网连接信息
    vpn_proxies = {
        'http': 'http://',
        'https': 'http://'
    }

    #是否显示消息记录
    verbose = False
