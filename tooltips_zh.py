#!/usr/bin/env python3
#
# 2018-10-23 05:24:32


class Widget_Mesg(object):
  def __init__(self, m):
    '''
    m: model.Model
    '''
    self.set_all_tooltips(m)
    self.set_all_placeholders(m)

  def set_all_placeholders(self, m):
    # 0.target区
    self._set_placeholder('通常是从 目标url/burp日志/HTTP请求... 中任选一项',
                          m._url_combobox.get_child())
    self._set_placeholder('-l: Burp或WebScarab代理的日志文件路径(用来解析目标)',
                          m._burp_logfile)
    self._set_placeholder('-r: 包含HTTP请求的的文件路径(如从fiddler中得来的)',
                          m._request_file)
    self._set_placeholder('-m: 给定一个包含多个目标的文本路径',
                          m._bulkfile)
    self._set_placeholder('-c: 从一个本地ini配置文件载入选项',
                          m._configfile)
    self._set_placeholder('-g: 将google dork的结果作为目标url',
                          m._google_dork)
    self._set_placeholder('-d: 直接连接远程DB的连接字符串',
                          m._direct_connect)
    # 选项区(page1)
    # 1.测试页面(Q)
    self._set_placeholder('id,user-agent',
                          m._inject_area_param_entry)
    self._set_placeholder('user-agent,referer',
                          m._inject_area_skip_entry)
    self._set_placeholder('token|session',
                          m._inject_area_param_exclude_entry)
    self._set_placeholder('用于闭合',
                          m._inject_area_prefix_entry)
    self._set_placeholder('user:password',
                          m._inject_area_dbms_cred_entry)
    self._set_placeholder('查询为真时页面出现的字串',
                          m._detection_area_str_entry)
    self._set_placeholder('查询为假时的',
                          m._detection_area_not_str_entry)
    self._set_placeholder('正则匹配查询为真时的字串',
                          m._detection_area_re_entry)
    self._set_placeholder('查询为真时的',
                          m._detection_area_code_entry)
    self._set_placeholder('BEUSTQ',
                          m._tech_area_tech_entry)
    self._set_placeholder('5',
                          m._tech_area_time_sec_entry)
    self._set_placeholder('10',
                          m._tech_area_union_col_entry)
    self._set_placeholder('NULL',
                          m._tech_area_union_char_entry)
    self._set_placeholder('有效表名',
                          m._tech_area_union_from_entry)
    self._set_placeholder('DNS exfiltration',
                          m._tech_area_dns_entry)
    # 2.请求页面(W)
    self._set_placeholder('e.g. X-Forwarded-For: 127.0.0.1',
                          m._request_area_header_entry)
    self._set_placeholder('e.g. Accept-Language: fr\\nETag: 123',
                          m._request_area_headers_entry)
    self._set_placeholder('post',
                          m._request_area_method_entry)
    self._set_placeholder('&',
                          m._request_area_param_del_entry)
    self._set_placeholder('query=foobar&id=1',
                          m._request_area_post_entry)
    self._set_placeholder('AU=233;SESSIONID=AABBCCDDEEFF;',
                          m._request_area_cookie_entry)
    self._set_placeholder(';',
                          m._request_area_cookie_del_entry)
    self._set_placeholder('Basic, Digest, NTLM or PKI',
                          m._request_area_auth_type_entry)
    self._set_placeholder('name:password',
                          m._request_area_auth_cred_entry)
    self._set_placeholder('PEM cert/private key file',
                          m._request_area_auth_file_entry)
    self._set_placeholder('post',
                          m._request_area_csrf_method_entry)
    self._set_placeholder('0',
                          m._request_area_csrf_retries_entry)
    self._set_placeholder('token字段名',
                          m._request_area_csrf_token_entry)
    self._set_placeholder('import hashlib;id2=hashlib.md5(id).hexdigest()',
                          m._request_area_eval_entry)
    # 3.枚举页面(E)
    self._set_placeholder('不包含该行',
                          m._limit_area_start_entry)
    self._set_placeholder('包含该行',
                          m._limit_area_stop_entry)
    self._set_placeholder('id<3',
                          m._meta_area_where_entry)
    # 4.文件页面(R)
    self._set_placeholder('配合 Meterpreter相关 使用',
                          m._os_access_area_msf_path_entry)
    # 5.其他页面(T)
    self._set_placeholder('sqlmap',
                          m._general_area_table_prefix_entry)
    self._set_placeholder('/var/www',
                          m._general_area_web_root_entry)
    self._set_placeholder(r'(www)?\.target\.(com|net|org)',
                          m._general_area_scope_entry)
    self._set_placeholder('ROW',
                          m._general_area_test_filter_entry)
    self._set_placeholder('BENCHMARK',
                          m._general_area_test_skip_entry)
    self._set_placeholder('CSV',
                          m._general_area_dump_format_entry)

    self._set_placeholder('不要加 http://',
                          m._page4_api_server_entry)
    self._set_placeholder('32位token',
                          m._page4_admin_token_entry)

  def set_all_tooltips(self, m):
    '''
    m: model.Model
    使用gtk3.24时, 有scale组件的行内的tooltip会flicker(闪烁)(GTK3的bug!)
    只能禁用了
    '''
    # 0.target区
    self._set_tooltip('必填项, 从 目标url/burp日志/HTTP请求... 任选一项',
                      m._url_combobox)
    self._set_tooltip('-l: Burp或WebScarab代理的日志文件路径(用来解析目标)',
                      m._burp_logfile)
    self._set_tooltip('-r: 包含HTTP请求的的文件路径(如从fiddler中得来的)',
                      m._request_file)
    self._set_tooltip('-m: 给定一个包含多个目标的文本路径',
                      m._bulkfile)
    self._set_tooltip('-c: 从一个本地ini配置文件载入选项',
                      m._configfile)
    self._set_tooltip('-g: 将google dork的结果作为目标url',
                      m._google_dork)
    # 选项区(page1)
    # 0._cmd_entry
    self._set_tooltip('1.勾选, 填写所需的 选项\n2.点击 收集选项\n3.点击 开始',
                      m._cmd_entry)
    # 1.测试页面(Q)
    self._set_tooltip('-p\n逗号分隔, 与--level不兼容',
                      m._inject_area_param_ckbtn,
                      m._inject_area_param_entry)
    self._set_tooltip('--param-filter=P..  Select testable parameter(s) by place (e.g. "POST")',
                      m._inject_area_param_filter_ckbtn,
                      m._inject_area_param_filter_combobox)
    self._set_tooltip('--skip-static\n'
        '另外: sqlmap不会针对(伪)静态网页(/param1/value1/),\n'
        '在任意(get/post/header等)可能的注入参数后加*即可',
                      m._inject_area_skip_static_ckbtn)
    self._set_tooltip('--skip=...,...  Skip testing for given parameter(s)',
                      m._inject_area_skip_ckbtn,
                      m._inject_area_skip_entry)
    self._set_tooltip('--param-exclude=.. Regexp to exclude parameters from testing',
                      m._inject_area_param_exclude_ckbtn,
                      m._inject_area_param_exclude_entry)
    self._set_tooltip('--prefix=PREFIX\n'
        '当情况复杂(如注入点位于嵌套JOIN查询中)时, 需要手动处理',
                      m._inject_area_prefix_ckbtn,
                      m._inject_area_prefix_entry)
    self._set_tooltip('--suffix=SUFFIX',
                      m._inject_area_suffix_ckbtn,
                      m._inject_area_suffix_entry)
    self._set_tooltip('--dbms=DBMS\n仅在确定是哪种DBMS时使用',
                      m._inject_area_dbms_ckbtn,
                      m._inject_area_dbms_combobox)
    self._set_tooltip('--dbms-cred=DBMS..  DBMS authentication credentials (user:password)',
                      m._inject_area_dbms_cred_ckbtn,
                      m._inject_area_dbms_cred_entry)
    self._set_tooltip('--os=OS\n仅在确定知道DBMS所在OS的名称时使用',
                      m._inject_area_os_ckbtn,
                      m._inject_area_os_entry)
    self._set_tooltip('--no-cast\n'
        '检索结果时, 默认会将条目cast为字符串类型(优化检索),\n'
        '若数据检索有问题(如某些老版本mysql), 才勾选',
                      m._inject_area_no_cast_ckbtn)
    self._set_tooltip('--no-escape\n'
        '注: 默认 select \'foobar\' 会变成 select char(102)+char(111)...\n'
        '    优点: 转义引号, 绕过; 缺点: 长度变长',
                      m._inject_area_no_escape_ckbtn)
    self._set_tooltip('--invalid-bignum\n'
        '真: id=13, 假: id=99999999',
                      m._inject_area_invalid_bignum_ckbtn)
    self._set_tooltip('--invalid-logical\n'
        '真: id=13, 假: id=13 AND 18=19',
                      m._inject_area_invalid_logical_ckbtn)
    self._set_tooltip('--invalid-string\n'
        '真: id=13, 假: id=akewmc',
                      m._inject_area_invalid_string_ckbtn)
    self._set_tooltip('--string=STRING',
                      m._detection_area_str_ckbtn,
                      m._detection_area_str_entry)
    self._set_tooltip('--not-string=NOT..',
                      m._detection_area_not_str_ckbtn,
                      m._detection_area_not_str_entry)
    self._set_tooltip('--regexp=',
                      m._detection_area_re_ckbtn,
                      m._detection_area_re_entry)
    self._set_tooltip('--code=',
                      m._detection_area_code_ckbtn,
                      m._detection_area_code_entry)
    self._set_tooltip('--text-only\n'
        '有的响应正文包含大量其他内容(如js脚本)\n'
        '勾选, 可让sqlmap仅关注文本内容',
                      m._detection_area_text_only_ckbtn)
    self._set_tooltip('--titles',
                      m._detection_area_titles_ckbtn)
    self._set_tooltip('--smart\n'
        '用于批量扫描(如-m时), 最快速地找出引发DBMS错误的目标,\n'
        '再对 可引发DBMS错误的参数 进一步扫描',
                      m._detection_area_smart_ckbtn)
    self._set_tooltip('--technique=B: Boolean-based blind\n'
                      '            E: Error-based\n'
                      '            U: Union query-based\n'
                      '            S: Stacked queries\n'
                      '            T: Time-based blind\n'
                      '            Q: Inline queries',
                      m._tech_area_tech_ckbtn,
                      m._tech_area_tech_entry)
    self._set_tooltip('--time-sec=默认5秒\n时间盲注时',
                      m._tech_area_time_sec_ckbtn,
                      m._tech_area_time_sec_entry)
    self._set_tooltip('--union-cols=默认10列\nunion查询时\n'
        '填12-16表示使用12到16列;\n'
        '提高level, 可增加至50列.',
                      m._tech_area_union_col_ckbtn,
                      m._tech_area_union_col_entry)
    self._set_tooltip('--union-char=默认使用NULL\nunion查询时\n'
        '如--union-char=001\n'
        '提高level, 会使用随机数',
                      m._tech_area_union_char_ckbtn,
                      m._tech_area_union_char_entry)
    self._set_tooltip('--union-from=\nunion查询时',
                      m._tech_area_union_from_ckbtn,
                      m._tech_area_union_from_entry)
    self._set_tooltip('--dns-domain=\n'
        '如果控制了目标url的DNS服务器, 才可使用此选项\n'
        '这样做只是用来加快数据检索',
                      m._tech_area_dns_ckbtn,
                      m._tech_area_dns_entry)
    self._set_tooltip('--second-url=',
                      m._tech_area_second_url_ckbtn,
                      m._tech_area_second_url_entry)
    self._set_tooltip('--second-req=',
                      m._tech_area_second_req_ckbtn,
                      m._tech_area_second_req_entry)
    # self._set_tooltip('sqlmap只会对CHAR()字符串进行混淆,\n'
    #     '不会对其他的payload进行任何混淆.\n'
    #     '要绕过IPS设备或Web应用防火墙(WAF)时, 使用此选项\n'
    #     '此处填写要使用的tamper脚本名, 回车或空格拼接\n'
    #     '详见: sqlmap --list-tampers',
    #                   m._tamper_area_tamper_view)
    self._set_tooltip('-o, 开启后会默认:\n'
        '  --keep-alive\n  --null-connection\n  --threads=3',
                      m._optimize_area_turn_all_ckbtn)
    self._set_tooltip('--threads=\n默认为1, 最大为10',
                      m._optimize_area_thread_num_ckbtn)
    self._set_tooltip('--predict-output\n'
        '此开关与--threads不兼容',
                      m._optimize_area_predict_ckbtn)
    self._set_tooltip('--keep-alive\n'
        '此开关与--proxy不兼容',
                      m._optimize_area_keep_alive_ckbtn)
    self._set_tooltip('--null-connection 盲注时\n'
        '此开关与--text-only不兼容\n'
        '有的请求类型可用来仅获取响应大小而不获取响应主体\n'
        '两种NULL连接技术: Range和HEAD',
                      m._optimize_area_null_connect_ckbtn)
    # -v:
    # 0: 只显示Python回源(tracebacks), 错误(error)和关键(criticle)信息。
    # 1: 同时显示信息(info)和警告信息（warning)（默认为1）
    # 2: 同时显示调试信息(debug)
    # 3: 同时显示注入的有效载荷(payloads)
    # 4: 同时显示http请求
    # 5: 同时显示http响应头
    # 6: 同时显示http响应内容
    # self._set_tooltip('-v 默认为1',
    #                   m._general_area_verbose_ckbtn)
    self._set_tooltip('--fingerprint\n'
        '默认就会自动指纹DB,\n'
        '开启此开关后, 会发送更多请求, 以确定更精确的DB/OS等版本信息',
                      m._general_area_finger_ckbtn)
    self._set_tooltip('--hex\n'
        '响应中的非ASCII数据不准确(如乱码)时, 会将其先编码成16进制格式',
                      m._general_area_hex_ckbtn)
    self._set_tooltip('--batch',
                      m._general_area_batch_ckbtn)
    self._set_tooltip('--wizard(其他选项可不选)',
                      m._misc_area_wizard_ckbtn)
    # 2.请求页面(W)
    self._set_tooltip('--random-agent\n'
        '默认, User-Agent: sqlmap/1.0-dev\n'
        '建议开启!',
                      m._request_area_random_agent_ckbtn)
    self._set_tooltip('--mobile',
                      m._request_area_mobile_ckbtn)
    self._set_tooltip('--user-agent=',
                      m._request_area_user_agent_ckbtn,
                      m._request_area_user_agent_entry)
    self._set_tooltip('--host=',
                      m._request_area_host_ckbtn,
                      m._request_area_host_entry)
    self._set_tooltip('--referer=\n'
        '默认情况下(即不加此参数)不会发送Referer报头',
                      m._request_area_referer_ckbtn,
                      m._request_area_referer_entry)
    self._set_tooltip('--header=',
                      m._request_area_header_ckbtn,
                      m._request_area_header_entry)
    self._set_tooltip('--headers=',
                      m._request_area_headers_ckbtn,
                      m._request_area_headers_entry)
    self._set_tooltip('--method=',
                      m._request_area_method_ckbtn,
                      m._request_area_method_entry)
    self._set_tooltip('--param-del=',
                      m._request_area_param_del_ckbtn,
                      m._request_area_param_del_entry)
    self._set_tooltip('--chunked',
                      m._request_area_chunked_ckbtn)
    self._set_tooltip('--data=\n'
        '默认情况下sqlmap发送的是GET请求, 若使用此参数, 会将数据post到目标\n'
        '比如搜索框, 表单等会通过post方式发送数据',
                      m._request_area_post_ckbtn,
                      m._request_area_post_entry)
    self._set_tooltip('--cookie=',
                      m._request_area_cookie_ckbtn,
                      m._request_area_cookie_entry)
    self._set_tooltip('--cookie-del=',
                      m._request_area_cookie_del_ckbtn,
                      m._request_area_cookie_del_entry)
    self._set_tooltip('--live-cookies=',
                      m._request_area_live_cookies_ckbtn,
                      m._request_area_live_cookies_entry)
    self._set_tooltip('--load-cookies=',
                      m._request_area_load_cookies_ckbtn,
                      m._request_area_load_cookies_entry)
    self._set_tooltip('--drop-set-cookie=',
                      m._request_area_drop_set_cookie_ckbtn)
    self._set_tooltip('--auth-type=Basic, Digest, NTLM or PKI',
                      m._request_area_auth_type_ckbtn,
                      m._request_area_auth_type_entry)
    self._set_tooltip('--auth-cred=',
                      m._request_area_auth_cred_ckbtn,
                      m._request_area_auth_cred_entry)
    self._set_tooltip('--auth-file=\n'
        'PEM格式的key_file, 包含你的证书和私钥',
                      m._request_area_auth_file_ckbtn,
                      m._request_area_auth_file_entry)
    self._set_tooltip('--csrf-method=',
                      m._request_area_csrf_method_ckbtn,
                      m._request_area_csrf_method_entry)
    self._set_tooltip('--csrf-retries=\n'
        'Retries for anti-CSRF token retrieval (default 0)',
                      m._request_area_csrf_retries_ckbtn,
                      m._request_area_csrf_retries_entry)
    self._set_tooltip('--csrf-token=\n'
        '如果表单中含有隐藏的随机token字段(用来防止csrf攻击的),\n'
        '使用此选项.',
                      m._request_area_csrf_token_ckbtn,
                      m._request_area_csrf_token_entry)
    self._set_tooltip('--csrf-url=\n'
        '若目标url没有token字段, 则指定有token字段的url',
                      m._request_area_csrf_url_ckbtn,
                      m._request_area_csrf_url_entry)
    self._set_tooltip('--ignore-timeouts',
                      m._request_area_ignore_timeouts_ckbtn)
    self._set_tooltip('--ignore-redirects',
                      m._request_area_ignore_redirects_ckbtn)
    self._set_tooltip('--ignore-code=',
                      m._request_area_ignore_code_ckbtn,
                      m._request_area_ignore_code_entry)
    self._set_tooltip('--skip-urlencode\n'
        '有的server只接受未编码的参数',
                      m._request_area_skip_urlencode_ckbtn)
    self._set_tooltip('--force-ssl',
                      m._request_area_force_ssl_ckbtn)
    self._set_tooltip('--hpp\n'
        '一种绕过WAF/IP/IDS的方法, 对ASP/IIS, ASP.NET/IIS特别有效',
                      m._request_area_hpp_ckbtn)
    self._set_tooltip('--delay=隔几秒发送一个HTTP请求',
                      m._request_area_delay_ckbtn,
                      m._request_area_delay_entry)
    self._set_tooltip('--timeout=',
                      m._request_area_timeout_ckbtn,
                      m._request_area_timeout_entry)
    self._set_tooltip('--retries=连接超时后的重连次数',
                      m._request_area_retries_ckbtn,
                      m._request_area_retries_entry)
    self._set_tooltip('--randomize=随机改变参数值',
                      m._request_area_randomize_ckbtn,
                      m._request_area_randomize_entry)
    self._set_tooltip('--eval=发送请求前先进行额外的处理(python code)',
                      m._request_area_eval_ckbtn,
                      m._request_area_eval_entry)
    self._set_tooltip('--safe-url=\n'
        '避免错误请求过多而被屏蔽, 顺便访问一下正常的页面',
                      m._request_area_safe_url_ckbtn,
                      m._request_area_safe_url_entry)
    self._set_tooltip('--safe-post=',
                      m._request_area_safe_post_ckbtn,
                      m._request_area_safe_post_entry)
    self._set_tooltip('--safe-req=',
                      m._request_area_safe_req_ckbtn,
                      m._request_area_safe_req_entry)
    self._set_tooltip('--safe-freq=SAFE.. Test requests between two visits to a given safe URL',
                      m._request_area_safe_freq_ckbtn,
                      m._request_area_safe_freq_entry)
    self._set_tooltip('--ignore-proxy Ignore system default proxy settings',
                      m._request_area_ignore_proxy_ckbtn)
    self._set_tooltip('--proxy-freq=PRO.. Requests between change of proxy from a given list',
                      m._request_area_proxy_freq_ckbtn,
                      m._request_area_proxy_freq_entry)
    self._set_tooltip('--proxy-file=',
                      m._request_area_proxy_file_ckbtn,
                      m._request_area_proxy_file_entry)
    self._set_tooltip('--proxy=',
                      m._request_area_proxy_ckbtn,
                      m._request_area_proxy_ip_label,
                      m._request_area_proxy_ip_entry,
                      m._request_area_proxy_port_label,
                      m._request_area_proxy_port_entry)
    self._set_tooltip('--proxy-cred=PRO.. Proxy authentication credentials (name:password)',
                      m._request_area_proxy_username_label,
                      m._request_area_proxy_username_entry,
                      m._request_area_proxy_password_label,
                      m._request_area_proxy_password_entry)
    self._set_tooltip('--tor',
                      m._request_area_tor_ckbtn)
    self._set_tooltip('--tor-port=',
                      m._request_area_tor_port_ckbtn,
                      m._request_area_tor_port_entry)
    self._set_tooltip('--tor-type=',
                      m._request_area_tor_type_ckbtn,
                      m._request_area_tor_type_entry)
    self._set_tooltip('--check-tor',
                      m._request_area_check_tor_ckbtn)
    # 3.枚举页面(E)
    self._set_tooltip('-b 获取DB banner(version()/@@version)',
                      m._enum_area_opts_ckbtns[0][0])
    self._set_tooltip('--current-user',
                      m._enum_area_opts_ckbtns[0][1])
    self._set_tooltip('--current-db',
                      m._enum_area_opts_ckbtns[0][2])
    self._set_tooltip('--hostname',
                      m._enum_area_opts_ckbtns[0][3])
    self._set_tooltip('--is-dba',
                      m._enum_area_opts_ckbtns[0][4])
    self._set_tooltip('--users',
                      m._enum_area_opts_ckbtns[1][0])
    self._set_tooltip('--passwords',
                      m._enum_area_opts_ckbtns[1][1])
    self._set_tooltip('--privileges\n'
        'sql server会显示是否每个用户都为dba, 而不是所有用户的权限列表',
                      m._enum_area_opts_ckbtns[1][2])
    self._set_tooltip('--roles 仅限oracle可用',
                      m._enum_area_opts_ckbtns[1][3])
    self._set_tooltip('--dbs',
                      m._enum_area_opts_ckbtns[1][4])
    self._set_tooltip('--tables\n'
        '若不指定-D, 会枚举所有库的表名',
                      m._enum_area_opts_ckbtns[2][0])
    self._set_tooltip('--columns\n'
        '所有列及数据类型, 可与-D, -T, -C配合\n'
        '若未指定-D, 则默认为当前库\n'
        'PostgreSQL: 需提供 public 或系统库的名称, 因为不可能枚举其他数据库表',
                      m._enum_area_opts_ckbtns[2][1])
    self._set_tooltip('--schema\n'
        '将枚举所有库, 表, 列及其各自类型\n'
        '建议配合--exclude-sysdbs, 数据量可能很大!',
                      m._enum_area_opts_ckbtns[2][2])
    self._set_tooltip('--count 表的条目数',
                      m._enum_area_opts_ckbtns[2][3])
    self._set_tooltip('--comments',
                      m._enum_area_opts_ckbtns[2][4])
    self._set_tooltip('--dump',
                      m._dump_area_dump_ckbtn)
    self._set_tooltip('--repair',
                      m._dump_area_repair_ckbtn)
    self._set_tooltip('--statements',
                      m._dump_area_statements_ckbtn)
    self._set_tooltip('--search 需配合以下选项使用:\n'
        '  -C=逗号分隔的列名: 将在所有DB中的所有表中 搜索指定列名\n'
        '  -T=逗号分隔的表名: 将在所有DB中 搜索指定表名\n'
        '  -D=逗号分隔的数据库名: 将 搜索指定库名\n',
                      m._dump_area_search_ckbtn)
    self._set_tooltip('--exclude-sysdbs\n'
        '注: sql server上 master库不视为系统库',
                      m._dump_area_no_sys_db_ckbtn)
    self._set_tooltip('--dump-all',
                      m._dump_area_dump_all_ckbtn)
    self._set_tooltip('--start=',
                      m._limit_area_start_ckbtn,
                      m._limit_area_start_entry)
    self._set_tooltip('--stop=',
                      m._limit_area_stop_ckbtn,
                      m._limit_area_stop_entry)
    self._set_tooltip('--first=',
                      m._blind_area_first_ckbtn,
                      m._blind_area_first_entry)
    self._set_tooltip('--last=',
                      m._blind_area_last_ckbtn,
                      m._blind_area_last_entry)
    self._set_tooltip('-D DB\n'
        'Oracle: 应指定TABLESPACE_NAME',
                      m._meta_area_D_ckbtn,
                      m._meta_area_D_entry)
    self._set_tooltip('-T TBL',
                      m._meta_area_T_ckbtn,
                      m._meta_area_T_entry)
    self._set_tooltip('-C COL',
                      m._meta_area_C_ckbtn,
                      m._meta_area_C_entry)
    self._set_tooltip('-U USER',
                      m._meta_area_U_ckbtn,
                      m._meta_area_U_entry)
    self._set_tooltip('-X EXCLUDE',
                      m._meta_area_X_ckbtn,
                      m._meta_area_X_entry)
    self._set_tooltip('--pivot-column=P\n'
        'for Microsoft SQL Server, Sybase and SAP MaxDB\n'
        '导出表数据时, 会自动选择合适的具有唯一值的列，一般是主键\n'
        '当自动选择的privot列不正确时使用此项',
                      m._meta_area_pivot_ckbtn,
                      m._meta_area_pivot_entry)
    self._set_tooltip('--where=',
                      m._meta_area_where_ckbtn,
                      m._meta_area_where_entry)
    self._set_tooltip('--sql-query=QUERY\n'
        '如果是select语句, 会获取结果;\n'
        '如果目标支持多语句查询, 会使用堆查询技术',
                      m._runsql_area_sql_query_ckbtn,
                      m._runsql_area_sql_query_entry)
    self._set_tooltip('--sql-shell\n支持TAB补全, 历史记录',
                      m._runsql_area_sql_shell_ckbtn)
    self._set_tooltip('--sql-file=SQLFILE',
                      m._runsql_area_sql_file_ckbtn,
                      m._runsql_area_sql_file_entry)
    self._set_tooltip('--common-tables\n'
        '有时--tables会失败, 通常原因如下:\n'
        '  1.MySQL<5.0: information_schema不存在\n'
        '  2.Access:    系统表(MSysObjects)默认不可读\n'
        '  3.--current-user没有 读取系统表的 权限\n'
        '  1和2的情况才能使用此选项(txt/common-tables.txt)',
                      m._brute_force_area_common_tables_ckbtn)
    self._set_tooltip('--common-columns(见--common-tables)',
                      m._brute_force_area_common_columns_ckbtn)
    self._set_tooltip('--common-files',
                      m._brute_force_area_common_files_ckbtn)
    # 4.文件页面(R)
    self._set_tooltip('远程DB所在主机上的文件路径\n'
        '前提: 1.MySQL, PostgreSQL或Microsoft SQL Server\n'
        '      2.当前用户有 读取文件的 相关权限',
                      m._file_read_area_file_read_ckbtn,
                      m._file_read_area_file_read_entry)
    self._set_tooltip('仅查看已下载到本地的文件',
                      m._file_read_area_file_read_btn)
    self._set_tooltip('--udf-inject  UDF即user-defined function\n'
        '将共享库上传到DB所在文件系统上, 来创建用户自定义的函数以供使用',
                      m._file_write_area_udf_ckbtn)
    self._set_tooltip('可选, 与--udf-inject配套使用',
                      m._file_write_area_shared_lib_ckbtn,
                      m._file_write_area_shared_lib_entry)
    self._set_tooltip('若使用此选项, 则--file-dest为必选项\n'
        '前提: 1.MySQL, PostgreSQL或Microsoft SQL Server\n'
        '      2.当前用户有 使用特定函数上传文件的 相关权限',
                      m._file_write_area_file_write_ckbtn,
                      m._file_write_area_file_write_entry)
    self._set_tooltip('上传到DB服务器中的文件名, 要求是绝对路径, 构造后会有引号!\n'
                      '与本地文件路径配套使用, 单独勾选无意义',
                      m._file_write_area_file_dest_ckbtn,
                      m._file_write_area_file_dest_entry)
    self._set_tooltip('--os-cmd=\n'
        '前提: 1.MySQL, PostgreSQL或Microsoft SQL Server\n'
        '      2.当前用户有相关权限\n'
        'MySQL或PostgreSQL: 上传包含sys_exec和sys_eval函数的共享库\n'
        'SQL Server: 使用xp_cmdshell存储过程. 若被禁用(>=2005), 就启用它;\n'
        '                                     若不存在, 就从新创建它',
                      m._os_access_area_os_cmd_ckbtn,
                      m._os_access_area_os_cmd_entry)
    self._set_tooltip('--os-shell\n支持TAB补全, 历史记录\n'
        '若不支持堆查询(如asp/php + MySQL), 且是MySQL(库站未分离!):\n'
        '  会使用SELECT子句INTO OUTFILE在可写目录创建一个web后门来执行命令\n'
        '  内置的web后门类型有: ASP, ASP.NET, JSP, PHP',
                      m._os_access_area_os_shell_ckbtn)
    self._set_tooltip('MySQL和PostgreSQL:\n'
        '  1.通过自带的UDF中的sys_bineval() 执行Metasploit的shellcode\n'
        '  2.通过自带的UDF中的sys_exec() 上传并执行Metasploit的stand-alone payload stager\n'
        'Microsoft SQL Server:\n'
        '  1.通过xp_cmdshell储存过程 上传并执行Metasploit的stand-alone payload stager\n',
                      m._os_access_area_os_pwn_ckbtn)
    self._set_tooltip('前提: 最高权限(linux: uid=0, windows: Administrator)\n'
        '      且目标 数据库以Windows管理员身份运行时\n'
        '  通过SMB攻击(MS08-068) 执行Metasploit的shellcode',
                      m._os_access_area_os_smbrelay_ckbtn)
    self._set_tooltip('SQL Server 2000, 2005:\n'
        '  通过sp_replwritetovarbin存储过程(MS09-004)溢出漏洞 执行Metasploit的payload\n'
        '  sqlmap用自带的exploit自动绕过DEP内存保护来触发漏洞, 但它依赖Metasploit来生成shellcode, 以便在成功利用后执行',
                      m._os_access_area_os_bof_ckbtn)
    self._set_tooltip('使用Metasploit的getsystem命令来提权\n'
        '注: windows:\n'
        '  MySQL: 默认以SYSTEM身份运行\n'
        '  Server 2000: 默认以SYSTEM身份运行\n'
        '  Server 2005-2008: 多数以NETWORK SERVICE, 少数以LOCAL SERVICE身份运行\n'
        '  PostgreSQL: 默认以低权限的用户postgres运行\n'
        '    linux:\n'
        '  PostgreSQL: 默认以低权限的用户postgres运行',
                      m._os_access_area_priv_esc_ckbtn)
    self._set_tooltip('--msf-path=',
                      m._os_access_area_msf_path_ckbtn,
                      m._os_access_area_msf_path_entry)
    self._set_tooltip('--tmp-path=TMPPATH Remote absolute path of temporary files directory',
                      m._os_access_area_tmp_path_ckbtn,
                      m._os_access_area_tmp_path_entry)
    self._set_tooltip('--reg-key=',
                      m._registry_area_reg_key_label,
                      m._registry_area_reg_key_entry)
    self._set_tooltip('--reg-value=',
                      m._registry_area_reg_value_label,
                      m._registry_area_reg_value_entry)
    self._set_tooltip('--reg-data=',
                      m._registry_area_reg_data_label,
                      m._registry_area_reg_data_entry)
    self._set_tooltip('--reg-type=',
                      m._registry_area_reg_type_label,
                      m._registry_area_reg_type_entry)
    # 5.其他页面(T)
    self._set_tooltip('--check-internet',
                      m._general_area_check_internet_ckbtn)
    self._set_tooltip('--fresh-queries',
                      m._general_area_fresh_queries_ckbtn)
    self._set_tooltip('--forms\n'
        '若想对 form表单参数 测试:\n'
        '  1.通过某些方式得到请求文件或表单参数\n'
        '  2.可用-r读取请求文件或--data指定表单参数\n'
        '但--forms开关: 可让sqlmap自行获取url响应中的表单参数 再做测试\n'
        '注: 是所有表单 及 所有表单参数',
                      m._general_area_forms_ckbtn)
    self._set_tooltip('--parse-errors',
                      m._general_area_parse_errors_ckbtn)
    self._set_tooltip('--cleanup\n'
        '清理 DBMS(如临时表sqlmapoutput, udf)及文件系统',
                      m._misc_area_cleanup_ckbtn)
    self._set_tooltip('--table-prefix=',
                      m._general_area_table_prefix_ckbtn,
                      m._general_area_table_prefix_entry)
    self._set_tooltip('--binary-fields=\n'
        '指定有二进制值的列, 获取该列数据时, 会转成16进制输出',
                      m._general_area_binary_fields_ckbtn,
                      m._general_area_binary_fields_entry)
    self._set_tooltip('--preprocess=',
                      m._general_area_preprocess_ckbtn,
                      m._general_area_preprocess_entry)
    self._set_tooltip('--postprocess=',
                      m._general_area_postprocess_ckbtn,
                      m._general_area_postprocess_entry)
    self._set_tooltip('--charset=  如获取SHA1密文时, 请求数可减小30%',
                      m._general_area_charset_ckbtn,
                      m._general_area_charset_entry)
    self._set_tooltip('--encoding=',
                      m._general_area_encoding_ckbtn,
                      m._general_area_encoding_entry)
    self._set_tooltip('--web-root=WEBROOT Web server document root directory (e.g. "/var/www")',
                      m._general_area_web_root_ckbtn,
                      m._general_area_web_root_entry)
    self._set_tooltip('--scope=SCOPE Regexp to filter targets from provided proxy log',
                      m._general_area_scope_ckbtn,
                      m._general_area_scope_entry)
    self._set_tooltip('--test-filter=TE.. Select tests by payloads and/or titles (e.g. ROW)',
                      m._general_area_test_filter_ckbtn,
                      m._general_area_test_filter_entry)
    self._set_tooltip('--test-skip=TEST.. Skip tests by payloads and/or titles (e.g. BENCHMARK)',
                      m._general_area_test_skip_ckbtn,
                      m._general_area_test_skip_entry)
    self._set_tooltip('--crawl=depth 爬取有漏洞的url',
                      m._general_area_crawl_ckbtn,
                      m._general_area_crawl_entry)
    self._set_tooltip('--crawl-exclude= 使用正则排除',
                      m._general_area_crawl_exclude_ckbtn,
                      m._general_area_crawl_exclude_entry)
    self._set_tooltip('-t TRAFFICFILE  Log all HTTP traffic into a textual file',
                      m._general_area_traffic_file_ckbtn,
                      m._general_area_traffic_file_entry)
    self._set_tooltip('--har=HARFILE  Log all HTTP traffic into a HAR file',
                      m._general_area_har_ckbtn,
                      m._general_area_har_entry)
    self._set_tooltip('--flush-session',
                      m._general_area_flush_session_ckbtn)
    self._set_tooltip('--dump-format=\nCSV(默认), HTML or SQLITE',
                      m._general_area_dump_format_ckbtn,
                      m._general_area_dump_format_entry)
    self._set_tooltip('--csv-del=',
                      m._general_area_csv_del_ckbtn,
                      m._general_area_csv_del_entry)
    self._set_tooltip('--save=SAVECONFIG  Save options to a configuration INI file',
                      m._general_area_save_ckbtn,
                      m._general_area_save_entry)
    self._set_tooltip('-s SESSIONFILE  Load session from a stored (.sqlite) file',
                      m._general_area_session_file_ckbtn,
                      m._general_area_session_file_entry)
    self._set_tooltip('--output-dir=',
                      m._general_area_output_dir_ckbtn,
                      m._general_area_output_dir_entry)
    self._set_tooltip('--skip-heuristics\n'
        'Skip heuristic detection of SQLi/XSS vulnerabilities',
                      m._misc_area_skip_heuristics_ckbtn)
    self._set_tooltip('--skip-waf\n'
        '默认情况, 会发送一个可疑的payload(所以有时明显没有防护还报警告)\n'
        '勾选以禁用此默认机制',
                      m._misc_area_skip_waf_ckbtn)
    self._set_tooltip('--unstable  Adjust options for unstable connections',
                      m._misc_area_unstable_ckbtn)
    self._set_tooltip('--list-tampers',
                      m._misc_area_list_tampers_ckbtn)
    self._set_tooltip('--sqlmap-shell',
                      m._misc_area_sqlmap_shell_ckbtn)
    self._set_tooltip('--disable-coloring',
                      m._misc_area_disable_color_ckbtn)
    self._set_tooltip('--eta',
                      m._general_area_eta_ckbtn)
    self._set_tooltip('--gpage=\n'
        '默认使用-g时, 会使用google的前100个URLs',
                      m._misc_area_gpage_ckbtn)
    self._set_tooltip('--beep',
                      m._misc_area_beep_ckbtn)
    self._set_tooltip('--offline',
                      m._misc_area_offline_ckbtn)
    self._set_tooltip('--purge 抹除$HOME/.sqlmap目录',
                      m._misc_area_purge_ckbtn)
    self._set_tooltip('--dependencies',
                      m._misc_area_dependencies_ckbtn)
    self._set_tooltip('--update',
                      m._misc_area_update_ckbtn)
    self._set_tooltip('--alert=ALERT Run host OS command(s) when SQL injection is found',
                      m._misc_area_alert_ckbtn,
                      m._misc_area_alert_entry)
    self._set_tooltip('--tmp-dir=TMPDIR Local directory for storing temporary files',
                      m._misc_area_tmp_dir_ckbtn,
                      m._misc_area_tmp_dir_entry)
    self._set_tooltip('--answers=ANSWERS Set question answers(e.g. "quit=N,follow=N")',
                      m._misc_area_answers_ckbtn,
                      m._misc_area_answers_entry)
    self._set_tooltip('-z MNEMONICS Use short mnemonics (e.g. "flu,bat,ban,tec=EU")',
                      m._misc_area_z_ckbtn,
                      m._misc_area_z_entry)
    self._set_tooltip('--results-file=R..  Location of CSV results file in multiple targets mode',
                      m._misc_area_results_file_ckbtn,
                      m._misc_area_results_file_entry)
    # API区(page4)
    self._set_tooltip('sqlmapapi.py -s --username="admin" --password="secret"',
                      m._page4_api_server_label,
                      m._page4_api_server_entry)
    self._set_tooltip('此处填写选项(空格分隔). 点击 "选项:" 查看',
                      m._page4_option_get_entry)
    _api_usage = '''sqlampapi HOW-TO:
    - server: sqlmapapi.py -s
    - client:
      1. input API server and Admin token
      2. click "create task"
      3. click "view tasks", tasks show up below
      4. input python dict type options to set here:
      {
        'url': 'http://www.site.com/vuln.php?id=1',
        'level': 1, 'risk': 1,
      }
      5. click "set:" to send the dict
      6. click start after sending the dict
      Note: 1. click "view tasks" to recheck tasks' status.
            2. sqlmapapi's options are not the same with sqlmap;
               sqlmapapi accept options, but won't verify it!
               delete the task whose option is invalid!
    '''
    self._set_tooltip(_api_usage,
                      m._page4_option_set_view)

  def _set_placeholder(self, placeholder, *widgets):
    '''
    widgets: mostly entry
    只有entry才有set_placeholder_text方法
    '''
    for _widget in widgets:
      _widget.set_placeholder_text(placeholder)

  def _set_tooltip(self, tooltip, *widgets):
    for _widget in widgets:
      _widget.set_tooltip_text(tooltip)


def main():
  from widgets import d, g
  from sqlmap_gtk import Window

  win = Window()

  css_provider = g.CssProvider.new()
  css_provider.load_from_path('static/css.css')
  g.StyleContext.add_provider_for_screen(
    d.Screen.get_default(),
    css_provider,
    g.STYLE_PROVIDER_PRIORITY_APPLICATION
  )

  win.connect('destroy', g.main_quit)
  win.show_all()
  g.main()


if __name__ == '__main__':
  main()
