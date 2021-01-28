#!/usr/bin/env python3
#
# 2020-12-31 01:55:43

import os
import gettext
from widgets import (g, Vte, Frame, btn, cb, cbb, et, label, sl, sp, tv)
from widgets import (FileEntry, NumberEntry)
from widgets import HORIZONTAL


class Model(object):

  def __init__(self, language):
    mo_filename = "sqlmap_gtk"
    mo_base_folder = os.path.abspath("static/locale")
    _ = self._
    try:
      if language == 'zh':
        lang_zh = gettext.translation(mo_filename, mo_base_folder, languages = ["zh_CN"])
        _ = lang_zh.gettext
    except FileNotFoundError as e:
      print(e)

    # 1. %s;(\('.*'\);(_(\1);g
    # 2. fix _enum_area_opts_ckbtns
    # TARGET
    self._url_combobox = cbb()
    self._burp_logfile = FileEntry()
    self._burp_logfile_chooser = btn.new_with_label(_('open'))
    self._request_file = FileEntry()
    self._request_file_chooser = btn.new_with_label(_('open'))
    self._bulkfile = FileEntry()
    self._bulkfile_chooser = btn.new_with_label(_('open'))
    self._configfile = FileEntry()
    self._configfile_chooser = btn.new_with_label(_('open'))
    self._google_dork = et()
    self._direct_connect = et()
  # OPTIONS(1)
  # collected options:
    self._cmd_entry = et()
  # Inject(Q)
    self._sqlmap_path_entry = FileEntry()
    self._sqlmap_path_chooser = btn.new_with_label(_('open'))
    # Injection
    self._injection_frame = Frame.new(_('Injection'))
    self._inject_area_param_ckbtn = cb(_('-p'))
    self._inject_area_param_entry = et()
    self._inject_area_param_filter_ckbtn = cb(_('--param-filter'))
    self._inject_area_param_filter_combobox = cbb()
    self._inject_area_skip_static_ckbtn = cb(_('--skip-static'))
    self._inject_area_skip_ckbtn = cb(_('--skip'))
    self._inject_area_skip_entry = et()
    self._inject_area_param_exclude_ckbtn = cb(_('--param-exclude'))
    self._inject_area_param_exclude_entry = et()
    self._inject_area_prefix_ckbtn = cb(_('--prefix'))
    self._inject_area_prefix_entry = et()
    self._inject_area_suffix_ckbtn = cb(_('--suffix'))
    self._inject_area_suffix_entry = et()
    self._inject_area_dbms_ckbtn = cb(_('--dbms'))
    self._inject_area_dbms_combobox = cbb()
    self._inject_area_dbms_cred_ckbtn = cb(_('--dbms-cred'))
    self._inject_area_dbms_cred_entry = et()
    self._inject_area_os_ckbtn = cb(_('--os'))
    self._inject_area_os_entry = et()
    self._inject_area_no_cast_ckbtn = cb(_('--no-cast'))
    self._inject_area_no_escape_ckbtn = cb(_('--no-escape'))
    self._inject_area_invalid_logical_ckbtn = cb(_('--invalid-logical'))
    self._inject_area_invalid_bignum_ckbtn = cb(_('--invalid-bignum'))
    self._inject_area_invalid_string_ckbtn = cb(_('--invalid-string'))
    # Detection
    self._detection_frame = Frame.new(_('Detection'))
    self._detection_area_level_ckbtn = cb(_('--level'))
    self._detection_area_level_scale = sl(HORIZONTAL, 1, 5, 1)
    self._detection_area_risk_ckbtn = cb(_('--risk'))
    self._detection_area_risk_scale = sl(HORIZONTAL, 1, 3, 1)
    self._detection_area_str_ckbtn = cb(_('--string'))
    self._detection_area_str_entry = et()
    self._detection_area_not_str_ckbtn = cb(_('--not-string'))
    self._detection_area_not_str_entry = et()
    self._detection_area_re_ckbtn = cb(_('--regexp'))
    self._detection_area_re_entry = et()
    self._detection_area_code_ckbtn = cb(_('--code'))
    self._detection_area_code_entry = NumberEntry()
    self._detection_area_text_only_ckbtn = cb(_('--text-only'))
    self._detection_area_titles_ckbtn = cb(_('--titles'))
    self._detection_area_smart_ckbtn = cb(_('--smart'))
    self._detection_area_level_note = label(label = _("Level 1(default): all GET, POST fields\n"
                                                      "Level 2   append: Cookie\n"
                                                      "Level 3   append: User-Agent/Referer\n"
                                                      "Level 4   append: ?\n"
                                                      "Level 5   append: Host header"),
                                            halign = g.Align.START)
    self._detection_area_risk_note = label(label = _("Risk 1(default): no risk\n"
                                                     "Risk 2   append: Time-Based Blind\n"
                                                     "Risk 3   append: \"OR\"-Based Blind"),
                                           halign = g.Align.START)
    # Technique
    self._tech_frame = Frame.new(_('Technique'))
    self._tech_area_tech_ckbtn = cb(_('--technique'))
    self._tech_area_tech_entry = et()
    self._tech_area_time_sec_ckbtn = cb(_('--time-sec'))
    self._tech_area_time_sec_entry = NumberEntry()
    self._tech_area_union_col_ckbtn = cb(_('--union-cols'))
    self._tech_area_union_col_entry = NumberEntry()
    self._tech_area_union_char_ckbtn = cb(_('--union-char'))
    self._tech_area_union_char_entry = et()
    self._tech_area_union_from_ckbtn = cb(_('--union-from'))
    self._tech_area_union_from_entry = et()
    self._tech_area_dns_ckbtn = cb(_('--dns-domain'))
    self._tech_area_dns_entry = et()
    self._tech_area_second_url_ckbtn = cb(_('--second-url'))
    self._tech_area_second_url_entry = et()
    self._tech_area_second_req_ckbtn = cb(_('--second-req:'))
    self._tech_area_second_req_entry = FileEntry()
    self._tech_area_second_req_chooser = btn.new_with_label(_('open'))
    # Tamper
    # self._tamper_frame = Frame.new(_('--tamper'))
    # self._tamper_area_tamper_view = tv(wrap_mode = g.WrapMode.CHAR)
    # Optimize
    self._optimize_frame = Frame.new(_('Optimize'))
    self._optimize_area_turn_all_ckbtn = cb(_('-o'))
    self._optimize_area_thread_num_ckbtn = cb(_('--threads'))
    self._optimize_area_thread_num_spinbtn = sp.new_with_range(2, 10, 1)
    self._optimize_area_predict_ckbtn = cb(_('--predict-output'))
    self._optimize_area_keep_alive_ckbtn = cb(_('--keep-alive'))
    self._optimize_area_null_connect_ckbtn = cb(_('--null-connection'))
    # Offen
    self._offen_frame = Frame.new(_('Offen'))
    self._general_area_verbose_ckbtn = cb(_('-v'))
    self._general_area_verbose_scale = sl(HORIZONTAL, 0, 6, 1)
    self._general_area_finger_ckbtn = cb(_('--fingerprint'))
    self._general_area_hex_ckbtn = cb(_('--hex'))
    self._general_area_batch_ckbtn = cb(_('--batch'))
    self._misc_area_wizard_ckbtn = cb(_('--wizard'))
    # Hidden
    self._hidden_frame = Frame.new(_('Hidden'))
    self._hidden_area_crack_ckbtn = cb(_('--crack'))
    self._hidden_area_debug_ckbtn = cb(_('--debug'))
    self._hidden_area_profile_ckbtn = cb(_('--profile'))
    self._hidden_area_disable_precon_ckbtn = cb(_('--disable-precon'))
    self._hidden_area_disable_stats_ckbtn = cb(_('--disable-stats'))
    self._hidden_area_force_dbms_ckbtn = cb(_('--force-dbms'))
    self._hidden_area_force_dns_ckbtn = cb(_('--force-dns'))
    self._hidden_area_force_pivoting_ckbtn = cb(_('--force-pivoting'))
    self._hidden_area_smoke_test_ckbtn = cb(_('--smoke-test'))
    self._hidden_area_live_test_ckbtn = cb(_('--live-test'))
    self._hidden_area_vuln_test_ckbtn = cb(_('--vuln-test'))
    self._hidden_area_murphy_rate_ckbtn = cb(_('--murphy-rate'))
    self._hidden_area_stop_fail_ckbtn = cb(_('--stop-fail'))
    self._hidden_area_run_case_ckbtn = cb(_('--run-case'))
    self._hidden_area_dummy_ckbtn = cb(_('--dummy'))
    self._hidden_area_api_ckbtn = cb(_('--api'))
    self._hidden_area_taskid_ckbtn = cb(_('--taskid'))
    self._hidden_area_database_ckbtn = cb(_('--database'))
  # Request(W)
    # HTTP header
    self._http_header_frame = Frame.new(_('HTTP header'))
    self._request_area_random_agent_ckbtn = cb(_('--random-agent'))
    self._request_area_mobile_ckbtn = cb(_('--mobile'))
    self._request_area_user_agent_ckbtn = cb(_('--user-agent'))
    self._request_area_user_agent_entry = et()
    self._request_area_host_ckbtn = cb(_('--host'))
    self._request_area_host_entry = et()
    self._request_area_referer_ckbtn = cb(_('--referer'))
    self._request_area_referer_entry = et()
    self._request_area_header_ckbtn = cb(_('--header(-H)'))
    self._request_area_header_entry = et()
    self._request_area_headers_ckbtn = cb(_('--headers'))
    self._request_area_headers_entry = et()
    # HTTP data
    self._http_data_frame = Frame.new(_('HTTP data'))
    self._request_area_method_ckbtn = cb(_('--method'))
    self._request_area_method_entry = et(width_chars = 10)
    self._request_area_param_del_ckbtn = cb(_('--param-del'))
    self._request_area_param_del_entry = et(max_length = 1, width_chars = 5)
    self._request_area_chunked_ckbtn = cb(_('--chunked'))
    self._request_area_post_ckbtn = cb(_('--data'))
    self._request_area_post_entry = et()
    self._request_area_cookie_ckbtn = cb(_('--cookie'))
    self._request_area_cookie_entry = et()
    self._request_area_cookie_del_ckbtn = cb(_('--cookie-del'))
    self._request_area_cookie_del_entry = et(width_chars = 5)
    self._request_area_drop_set_cookie_ckbtn = cb(_('--drop-set-cookie'))
    self._request_area_live_cookies_ckbtn = cb(_('--live-cookies'))
    self._request_area_live_cookies_entry = FileEntry()
    self._request_area_live_cookies_chooser = btn.new_with_label(_('open'))
    self._request_area_load_cookies_ckbtn = cb(_('--load-Cookies'))
    self._request_area_load_cookies_entry = FileEntry()
    self._request_area_load_cookies_chooser = btn.new_with_label(_('open'))
    self._request_area_auth_type_ckbtn = cb(_('--auth-type'))
    self._request_area_auth_type_entry = et()
    self._request_area_auth_cred_ckbtn = cb(_('--auth-cred'))
    self._request_area_auth_cred_entry = et()
    self._request_area_auth_file_ckbtn = cb(_('--auth-file'))
    self._request_area_auth_file_entry = FileEntry()
    self._request_area_auth_file_chooser = btn.new_with_label(_('open'))
    self._request_area_csrf_method_ckbtn = cb(_('--csrf-method'))
    self._request_area_csrf_method_entry = et(width_chars = 10)
    self._request_area_csrf_retries_ckbtn = cb(_('--csrf-retries'))
    self._request_area_csrf_retries_entry = NumberEntry()
    self._request_area_csrf_token_ckbtn = cb(_('--csrf-token'))
    self._request_area_csrf_token_entry = et()
    self._request_area_csrf_url_ckbtn = cb(_('--csrf-url'))
    self._request_area_csrf_url_entry = et()
    # Request custom
    self._request_custom_frame = Frame.new(_('Request custom'))
    self._request_area_ignore_timeouts_ckbtn = cb(_('--ignore-timeouts'))
    self._request_area_ignore_redirects_ckbtn = cb(_('--ignore-redirects'))
    self._request_area_ignore_code_ckbtn = cb(_('--ignore-code'))
    self._request_area_ignore_code_entry = et(text = '401', width_chars = 30)
    self._request_area_skip_urlencode_ckbtn = cb(_('--skip-urlencode'))
    self._request_area_force_ssl_ckbtn = cb(_('--force-ssl'))
    self._request_area_hpp_ckbtn = cb(_('--hpp'))
    self._request_area_delay_ckbtn = cb(_('--delay'))
    self._request_area_delay_entry = NumberEntry()
    self._request_area_timeout_ckbtn = cb(_('--timeout'))
    self._request_area_timeout_entry = NumberEntry()
    self._request_area_retries_ckbtn = cb(_('--retries'))
    self._request_area_retries_entry = NumberEntry()
    self._request_area_randomize_ckbtn = cb(_('--randomize'))
    self._request_area_randomize_entry = et()
    self._request_area_eval_ckbtn = cb(_('--eval'))
    self._request_area_eval_entry = et()
    # Anonymous/Proxy
    self._anonymous_Proxy_frame = Frame.new(_('Anonymous/Proxy'))
    self._request_area_safe_url_ckbtn = cb(_('--safe-url'))
    self._request_area_safe_url_entry = et()
    self._request_area_safe_post_ckbtn = cb(_('--safe-post'))
    self._request_area_safe_post_entry = et()
    self._request_area_safe_req_ckbtn = cb(_('--safe-req'))
    self._request_area_safe_req_entry = FileEntry()
    self._request_area_safe_req_chooser = btn.new_with_label(_('open'))
    self._request_area_safe_freq_ckbtn = cb(_('--safe-freq'))
    self._request_area_safe_freq_entry = et(width_chars = 10)
    self._request_area_ignore_proxy_ckbtn = cb(_('--ignore-proxy'))
    self._request_area_proxy_freq_ckbtn = cb(_('--proxy-freq'))
    self._request_area_proxy_freq_entry = NumberEntry()
    self._request_area_proxy_file_ckbtn = cb(_('--proxy-file'))
    self._request_area_proxy_file_entry = FileEntry()
    self._request_area_proxy_file_chooser = btn.new_with_label(_('open'))
    self._request_area_proxy_ckbtn = cb(_('--proxy'))
    self._request_area_proxy_ip_label = label.new('IP:')
    self._request_area_proxy_ip_entry = et()
    self._request_area_proxy_port_label = label.new('PORT:')
    self._request_area_proxy_port_entry = NumberEntry()
    self._request_area_proxy_username_label = label.new(_('username:'))
    self._request_area_proxy_username_entry = et()
    self._request_area_proxy_password_label = label.new(_('password:'))
    self._request_area_proxy_password_entry = et()
    self._request_area_tor_ckbtn = cb(_('--tor'))
    self._request_area_tor_port_ckbtn = cb(_('--tor-port'))
    self._request_area_tor_port_entry = NumberEntry()
    self._request_area_tor_type_ckbtn = cb(_('--tor-type'))
    self._request_area_tor_type_entry = et()
    self._request_area_check_tor_ckbtn = cb(_('--check-tor'))
  # Enumerate(E)
    # Enumeration
    self._enumeration_frame = Frame.new(_('Enumeration'))
    self._enum_area_opts_ckbtns = (
      (cb(_('--banner')), cb(_('--current-user')), cb(_('--current-db')), cb(_('--hostname')), cb(_('--is-dba'))),
      (cb(_('--users')), cb(_('--passwords')), cb(_('--privileges')), cb(_('--roles')), cb(_('--dbs'))),
      (cb(_('--tables')), cb(_('--columns')), cb(_('--schema')), cb(_('--count')), cb(_('--comments'))),
    )
    # Dump
    self._dump_frame = Frame.new(_('Dump'))
    self._dump_area_dump_ckbtn = cb(_('--dump'))
    self._dump_area_repair_ckbtn = cb(_('--repair'))
    self._dump_area_statements_ckbtn = cb(_('--statements'))
    self._dump_area_search_ckbtn = cb(_('--search'))
    self._dump_area_no_sys_db_ckbtn = cb(_('--exclude-sysdb'))
    self._dump_area_dump_all_ckbtn = cb(_('--dump-all'))
    # Limit(when dump)
    self._limit_frame = Frame.new(_('Limit'))
    self._limit_area_start_ckbtn = cb(_('--start'))
    self._limit_area_start_entry = NumberEntry()
    self._limit_area_stop_ckbtn = cb(_('--stop'))
    self._limit_area_stop_entry = NumberEntry()
    # Blind inject options
    self._blind_options_frame = Frame.new(_('Blind inject options'))
    self._blind_area_first_ckbtn = cb(_('--first'))
    self._blind_area_first_entry = NumberEntry()
    self._blind_area_last_ckbtn = cb(_('--last'))
    self._blind_area_last_entry = NumberEntry()
    # DB, Table, Column name...
    self._DTC_name_frame = Frame.new(_('DB, Table, Column name...'))
    self._meta_area_D_ckbtn = cb(_('-D'))
    self._meta_area_D_entry = et()
    self._meta_area_T_ckbtn = cb(_('-T'))
    self._meta_area_T_entry = et()
    self._meta_area_C_ckbtn = cb(_('-C'))
    self._meta_area_C_entry = et()
    self._meta_area_U_ckbtn = cb(_('-U'))
    self._meta_area_U_entry = et()
    self._meta_area_X_ckbtn = cb(_('-X'))
    self._meta_area_X_entry = et()
    self._meta_area_pivot_ckbtn = cb(_('--pivot-column'))
    self._meta_area_pivot_entry = et()
    self._meta_area_where_ckbtn = cb(_('--where'))
    self._meta_area_where_entry = et()
    # Execute SQL
    self._execute_sql_frame = Frame.new(_('Execute SQL'))
    self._runsql_area_sql_query_ckbtn = cb(_('--sql-query'))
    self._runsql_area_sql_query_entry = et()
    self._runsql_area_sql_shell_ckbtn = cb(_('--sql-shell'))
    self._runsql_area_sql_file_ckbtn = cb(_('--sql-file'))
    self._runsql_area_sql_file_entry = FileEntry()
    self._runsql_area_sql_file_chooser = btn.new_with_label(_('open'))
    # Brute force
    self._brute_force_frame = Frame.new(_('Brute force'))
    self._brute_force_area_common_tables_ckbtn = cb(_('--common-tables'))
    self._brute_force_area_common_columns_ckbtn = cb(_('--common-columns'))
    self._brute_force_area_common_files_ckbtn = cb(_('--common-files'))
  # File(R)
    # Read remote file
    self._read_remote_file_frame = Frame.new(_('Read remote file'))
    self._file_read_area_file_read_ckbtn = cb(_('--file-read'))
    self._file_read_area_file_read_entry = et(text = '/etc/passwd')
    self._file_read_area_file_read_btn = btn.new_with_label(_('cat'))
    # Upload local file
    self._upload_local_file_frame = Frame.new(_('Upload local file'))
    self._file_write_area_udf_ckbtn = cb(_('--udf-inject'))
    self._file_write_area_shared_lib_ckbtn = cb(_('--shared-lib'))
    self._file_write_area_shared_lib_entry = FileEntry()
    self._file_write_area_shared_lib_chooser = btn.new_with_label(_('open'))
    self._file_write_area_file_write_ckbtn = cb(_('--file-write'))
    self._file_write_area_file_write_entry = FileEntry()
    self._file_write_area_file_write_chooser = btn.new_with_label(_('open'))
    self._file_write_area_file_dest_ckbtn = cb(_('--file-dest'))
    self._file_write_area_file_dest_entry = et()
    # Access to the OS behind the DBMS
    self._os_access_frame = Frame.new(_('Access to the OS behind the DBMS'))
    self._os_access_area_os_cmd_ckbtn = cb(_('--os-cmd'))
    self._os_access_area_os_cmd_entry = et()
    self._os_access_area_os_shell_ckbtn = cb(_('--os-shell'))
    self._os_access_area_os_pwn_ckbtn = cb('--os-pwn')
    self._os_access_area_os_smbrelay_ckbtn = cb('--os-smbrelay')
    self._os_access_area_os_bof_ckbtn = cb('--os-bof')
    self._os_access_area_priv_esc_ckbtn = cb('--priv-esc')
    self._os_access_area_msf_path_ckbtn = cb(_('--msf-path'))
    self._os_access_area_msf_path_entry = FileEntry()
    self._os_access_area_msf_path_chooser = btn.new_with_label(_('open'))
    self._os_access_area_tmp_path_ckbtn = cb(_('--tmp-path'))
    self._os_access_area_tmp_path_entry = et()
    # Access to register in remote WIN
    self._registry_frame = Frame.new(_('Access to register in remote WIN'))
    self._registry_area_reg_ckbtn = cb(_('operate:'))
    self._registry_area_reg_combobox = g.ComboBoxText.new()
    self._registry_area_reg_key_label = label.new(_('--reg-key'))
    self._registry_area_reg_key_entry = et()
    self._registry_area_reg_value_label = label.new(_('--reg-value'))
    self._registry_area_reg_value_entry = et()
    self._registry_area_reg_data_label = label.new(_('--reg-data'))
    self._registry_area_reg_data_entry = et()
    self._registry_area_reg_type_label = label.new(_('--reg-type'))
    self._registry_area_reg_type_entry = et()
  # Other(T)
    # General
    self._general_frame = Frame.new(_('General'))
    self._general_area_check_internet_ckbtn = cb(_('--check-internet'))
    self._general_area_fresh_queries_ckbtn = cb(_('--fresh-queries'))
    self._general_area_forms_ckbtn = cb(_('--forms'))
    self._general_area_parse_errors_ckbtn = cb(_('--parse-errors'))
    self._misc_area_cleanup_ckbtn = cb(_('--cleanup'))
    self._general_area_base64_ckbtn = cb(_('--base64'))
    self._general_area_base64_entry = et()
    self._general_area_base64_safe_ckbtn = cb(_('--base64-safe'))
    self._general_area_table_prefix_ckbtn = cb(_('--table-prefix'))
    self._general_area_table_prefix_entry = et(width_chars = 15)
    self._general_area_binary_fields_ckbtn = cb(_('--binary-fields'))
    self._general_area_binary_fields_entry = et()
    self._general_area_preprocess_ckbtn = cb(_('--preprocess'))
    self._general_area_preprocess_entry = et()
    self._general_area_preprocess_chooser = btn.new_with_label(_('open'))
    self._general_area_postprocess_ckbtn = cb(_('--postprocess'))
    self._general_area_postprocess_entry = et()
    self._general_area_postprocess_chooser = btn.new_with_label(_('open'))
    self._general_area_charset_ckbtn = cb(_('--charset'))
    self._general_area_charset_entry = et(text = '0123456789abcdef')
    self._general_area_encoding_ckbtn = cb(_('--encoding'))
    self._general_area_encoding_entry = et(text = 'GBK', width_chars = 10)
    self._general_area_web_root_ckbtn = cb(_('--web-root'))
    self._general_area_web_root_entry = et()
    self._general_area_scope_ckbtn = cb(_('--scope'))
    self._general_area_scope_entry = FileEntry()
    self._general_area_scope_chooser = btn.new_with_label(_('open'))
    self._general_area_test_filter_ckbtn = cb(_('--test-filter'))
    self._general_area_test_filter_entry = et()
    self._general_area_test_skip_ckbtn = cb(_('--test-skip'))
    self._general_area_test_skip_entry = et()
    self._general_area_crawl_ckbtn = cb(_('--crawl'))
    self._general_area_crawl_entry = NumberEntry()
    self._general_area_crawl_exclude_ckbtn = cb(_('--crawl-exclude'))
    self._general_area_crawl_exclude_entry = et()
    self._general_area_traffic_file_ckbtn = cb(_('-t'))
    self._general_area_traffic_file_entry = FileEntry()
    self._general_area_traffic_file_chooser = btn.new_with_label(_('open'))
    self._general_area_har_ckbtn = cb(_('--har'))
    self._general_area_har_entry = FileEntry()
    self._general_area_har_chooser = btn.new_with_label(_('open'))
    self._general_area_flush_session_ckbtn = cb("<b>%s</b>" % '--flush-session')
    self._general_area_dump_format_ckbtn = cb(_('--dump-format'))
    self._general_area_dump_format_entry = et(width_chars = 6)
    self._general_area_csv_del_ckbtn = cb(_('--csv-del'))
    self._general_area_csv_del_entry = et(text = ',', max_length = 1, width_chars = 5)
    self._general_area_save_ckbtn = cb(_('--save'))
    self._general_area_save_entry = FileEntry()
    self._general_area_save_chooser = btn.new_with_label(_('open'))
    self._general_area_session_file_ckbtn = cb(_('-s'))
    self._general_area_session_file_entry = FileEntry()
    self._general_area_session_file_chooser = btn.new_with_label(_('open'))
    self._general_area_output_dir_ckbtn = cb(_('--output-dir'))
    self._general_area_output_dir_entry = FileEntry()
    self._general_area_output_dir_chooser = btn.new_with_label(_('open'))
    # Misc
    self._misc_frame = Frame.new(_('Misc'))
    self._misc_area_skip_heuristics_ckbtn = cb(_('--skip-heuristics'))
    self._misc_area_skip_waf_ckbtn = cb(_('--skip-waf'))
    self._misc_area_unstable_ckbtn = cb(_('--unstable'))
    self._misc_area_list_tampers_ckbtn = cb(_('--list-tampers'))
    self._misc_area_sqlmap_shell_ckbtn = cb(_('--sqlmap-shell'))
    self._misc_area_disable_color_ckbtn = cb(_('--disable-coloring'))
    self._general_area_eta_ckbtn = cb(_('--eta'))
    self._misc_area_gpage_ckbtn = cb(_('--gpage'))
    self._misc_area_gpage_spinbtn = sp.new_with_range(1, 100, 1)
    self._misc_area_beep_ckbtn = cb(_('--beep'))
    self._misc_area_offline_ckbtn = cb(_('--offline'))
    self._misc_area_purge_ckbtn = cb("<b>%s</b>" % '--purge')
    self._misc_area_dependencies_ckbtn = cb(_('--dependencies'))
    self._misc_area_update_ckbtn = cb(_('--update'))
    self._misc_area_alert_ckbtn = cb(_('--alert'))
    self._misc_area_alert_entry = et()
    self._misc_area_tmp_dir_ckbtn = cb(_('--tmp-dir'))
    self._misc_area_tmp_dir_entry = FileEntry()
    self._misc_area_tmp_dir_chooser = btn.new_with_label(_('open'))
    self._misc_area_answers_ckbtn = cb(_('--answers'))
    self._misc_area_answers_entry = et(text = 'quit=N,follow=N')
    self._misc_area_z_ckbtn = cb(_('-z'))
    self._misc_area_z_entry = et(text = 'flu,bat,ban,tec=EU...')
    self._misc_area_results_file_ckbtn = cb(_('--results-file'))
    self._misc_area_results_file_entry = FileEntry()
    self._misc_area_results_file_chooser = btn.new_with_label(_('open'))
  # Tamper
    self._tampers()
  # EXECUTION(2)
    self._page2_respwan_btn = btn.new_with_label(_('reopen'))
    self._page2_right_btn = btn.new_with_label(_('context menu'))
    self._page2_terminal = Vte.Terminal.new()
  # LOG(3)
    self._page3_log_view = tv(editable = False, wrap_mode = g.WrapMode.WORD)
    self._page3_read_target_btn = btn.new_with_label(_('view target file'))
    self._page3_clear_btn = btn.new_with_mnemonic(_('clear buffer(_C)'))
    self._page3_read_log_btn = btn.new_with_label(_('view log file'))
  # SQLMAPAPI(4)
    self._page4_api_server_label = label.new('REST-JSON API server:')
    self._page4_api_server_entry = et(text = '127.0.0.1:8775')
    self._page4_admin_token_label = label.new('Admin (secret) token:')
    self._page4_admin_token_entry = et(max_length = 32)
    self._page4_task_new_btn = btn.new_with_label(_('create task'))
    self._page4_admin_list_btn = btn.new_with_label(_('view tasks'))
    self._page4_admin_flush_btn = btn.new_with_label(_('delete all tasks'))
    self._page4_clear_task_view_btn = btn.new_with_label(_('clear view'))
    self._page4_username_label = label.new(_('username:'))
    self._page4_username_entry = et()
    self._page4_password_label = label.new(_('passwd:'))
    self._page4_password_entry = et()
    self._page4_option_get_entry = et(text = 'url risk level')
    self._page4_option_set_view = tv(wrap_mode = g.WrapMode.CHAR)
    self._page4_task_view = tv(editable = False, wrap_mode = g.WrapMode.WORD)
  # HELP(H)
    self._page5_manual_view = tv(editable = False, wrap_mode = g.WrapMode.WORD)
  # ABOUT
    self._page6_lang_en_radio = g.RadioButton.new_with_label_from_widget(None, 'en')
    self._page6_lang_zh_radio = g.RadioButton.new_from_widget(self._page6_lang_en_radio)
    self._page6_lang_zh_radio.set_label('zh')
    self._page6_tooltips_en_radio = g.RadioButton.new_with_label_from_widget(None, 'en')
    self._page6_tooltips_zh_radio = g.RadioButton.new_from_widget(self._page6_tooltips_en_radio)
    self._page6_tooltips_zh_radio.set_label('zh')

  def _tampers(self):
    self._tampers_name = [
      cb('0eunion.py'), cb('apostrophemask.py'), cb('apostrophenullencode.py'),
      cb('appendnullbyte.py'), cb('base64encode.py'), cb('between.py'),
      cb('binary.py'), cb('bluecoat.py'), cb('chardoubleencode.py'),
      cb('charencode.py'), cb('charunicodeencode.py'), cb('charunicodeescape.py'),
      cb('commalesslimit.py'), cb('commalessmid.py'), cb('commentbeforeparentheses.py'),
      cb('concat2concatws.py'), cb('dunion.py'), cb('equaltolike.py'),
      cb('equaltorlike.py'), cb('escapequotes.py'), cb('greatest.py'),
      cb('halfversionedmorekeywords.py'), cb('hex2char.py'), cb('htmlencode.py'),
      cb('ifnull2casewhenisnull.py'), cb('ifnull2ifisnull.py'), cb('informationschemacomment.py'),
      cb('least.py'), cb('lowercase.py'), cb('luanginx.py'),
      cb('misunion.py'), cb('modsecurityversioned.py'), cb('modsecurityzeroversioned.py'),
      cb('multiplespaces.py'), cb('overlongutf8.py'), cb('overlongutf8more.py'),
      cb('percentage.py'), cb('plus2concat.py'), cb('plus2fnconcat.py'),
      cb('randomcase.py'), cb('randomcomments.py'), cb('schemasplit.py'),
      cb('sleep2getlock.py'), cb('sp_password.py'), cb('space2comment.py'),
      cb('space2dash.py'), cb('space2hash.py'), cb('space2morecomment.py'),
      cb('space2morehash.py'), cb('space2mssqlblank.py'), cb('space2mssqlhash.py'),
      cb('space2mysqlblank.py'), cb('space2mysqldash.py'), cb('space2plus.py'),
      cb('space2randomblank.py'), cb('substring2leftright.py'), cb('symboliclogical.py'),
      cb('unionalltounion.py'), cb('unmagicquotes.py'), cb('uppercase.py'),
      cb('varnish.py'), cb('versionedkeywords.py'), cb('versionedmorekeywords.py'),
      cb('xforwardedfor.py'),
    ]
    self._tampers_label = [
      label.new(r"Replaces instances of <int> UNION with <int>e0UNION"),
      label.new(r"Replaces apostrophe character (') with its UTF-8 full width counterpart (e.g. ' -> %EF%BC%87)"),
      label.new(r"Replaces apostrophe character (') with its illegal double unicode counterpart (e.g. ' -> %00%27)"),
      label.new(r"Appends (Access) NULL byte character (%00) at the end of payload"),
      label.new(r"Base64-encodes all characters in a given payload"),
      label.new(r"Replaces greater than operator ('>') with 'NOT BETWEEN 0 AND #' and equals operator ('=') with 'BETWEEN # AND #'"),
      label.new(r"Injects keyword binary where possible"),
      label.new(r"Replaces space character after SQL statement with a valid random blank character. Afterwards replace character '=' with operator LIKE"),
      label.new(r"Double URL-encodes all characters in a given payload (not processing already encoded) (e.g. SELECT -> %2553%2545%254C%2545%2543%2554)"),
      label.new(r"URL-encodes all characters in a given payload (not processing already encoded) (e.g. SELECT -> %53%45%4C%45%43%54)"),
      label.new(r"Unicode-URL-encodes all characters in a given payload (not processing already encoded) (e.g. SELECT -> %u0053%u0045%u004C%u0045%u0043%u0054)"),
      label.new(r"Unicode-escapes non-encoded characters in a given payload (not processing already encoded) (e.g. SELECT -> \u0053\u0045\u004C\u0045\u0043\u0054)"),
      label.new(r"Replaces (MySQL) instances like 'LIMIT M, N' with 'LIMIT N OFFSET M' counterpart"),
      label.new(r"Replaces (MySQL) instances like 'MID(A, B, C)' with 'MID(A FROM B FOR C)' counterpart"),
      label.new(r"Prepends (inline) comment before parentheses (e.g. ( -> /**/()"),
      label.new(r"Replaces (MySQL) instances like 'CONCAT(A, B)' with 'CONCAT_WS(MID(CHAR(0), 0, 0), A, B)' counterpart"),
      label.new(r"Replaces instances of <int> UNION with <int>DUNION"),
      label.new(r"Replaces all occurrences of operator equal ('=') with 'LIKE' counterpart"),
      label.new(r"Replaces all occurrences of operator equal ('=') with 'RLIKE' counterpart"),
      label.new(r"Slash escape single and double quotes (e.g. ' -> \')"),
      label.new(r"Replaces greater than operator ('>') with 'GREATEST' counterpart"),
      label.new(r"Adds (MySQL) versioned comment before each keyword"),
      label.new(r"Replaces each (MySQL) 0x<hex> encoded string with equivalent CONCAT(CHAR(),...) counterpart"),
      label.new(r"HTML encode (using code points) all non-alphanumeric characters (e.g. ' -> &#39;)"),
      label.new(r"Replaces instances like 'IFNULL(A, B)' with 'CASE WHEN ISNULL(A) THEN (B) ELSE (A) END' counterpart"),
      label.new(r"Replaces instances like 'IFNULL(A, B)' with 'IF(ISNULL(A), B, A)' counterpart"),
      label.new(r"Add an inline comment (/**/) to the end of all occurrences of (MySQL) \"information_schema\" identifier"),
      label.new(r"Replaces greater than operator ('>') with 'LEAST' counterpart"),
      label.new(r"Replaces each keyword character with lower case value (e.g. SELECT -> select)"),
      label.new(r"LUA-Nginx WAFs Bypass (e.g. Cloudflare)"),
      label.new(r"Replaces instances of UNION with -.1UNION"),
      label.new(r"Embraces complete query with (MySQL) versioned comment"),
      label.new(r"Embraces complete query with (MySQL) zero-versioned comment"),
      label.new(r"Adds multiple spaces (' ') around SQL keywords"),
      label.new(r"Converts all (non-alphanum) characters in a given payload to overlong UTF8 (not processing already encoded) (e.g. ' -> %C0%A7)"),
      label.new(r"Converts all characters in a given payload to overlong UTF8 (not processing already encoded) (e.g. SELECT -> %C1%93%C1%85%C1%8C%C1%85%C1%83%C1%94)"),
      label.new(r"Adds a percentage sign ('%') infront of each character (e.g. SELECT -> %S%E%L%E%C%T)"),
      label.new(r"Replaces plus operator ('+') with (MsSQL) function CONCAT() counterpart"),
      label.new(r"Replaces plus operator ('+') with (MsSQL) ODBC function {fn CONCAT()} counterpart"),
      label.new(r"Replaces each keyword character with random case value (e.g. SELECT -> SEleCt)"),
      label.new(r"Add random inline comments inside SQL keywords (e.g. SELECT -> S/**/E/**/LECT)"),
      label.new(r"Splits FROM schema identifiers (e.g. 'testdb.users') with whitespace (e.g. 'testdb 9.e.users')"),
      label.new(r"Replaces instances like 'SLEEP(5)' with (e.g.) \"GET_LOCK('ETgP',5)\""),
      label.new(r"Appends (MsSQL) function 'sp_password' to the end of the payload for automatic obfuscation from DBMS logs"),
      label.new(r"Replaces space character (' ') with comments '/**/'"),
      label.new(r"Replaces space character (' ') with a dash comment ('--') followed by a random string and a new line ('\n')"),
      label.new(r"Replaces (MySQL) instances of space character (' ') with a pound character ('#') followed by a random string and a new line ('\n')"),
      label.new(r"Replaces (MySQL) instances of space character (' ') with comments '/**_**/'"),
      label.new(r"Replaces (MySQL) instances of space character (' ') with a pound character ('#') followed by a random string and a new line ('\n')"),
      label.new(r"Replaces (MsSQL) instances of space character (' ') with a random blank character from a valid set of alternate characters"),
      label.new(r"Replaces space character (' ') with a pound character ('#') followed by a new line ('\n')"),
      label.new(r"Replaces (MySQL) instances of space character (' ') with a random blank character from a valid set of alternate characters"),
      label.new(r"Replaces space character (' ') with a dash comment ('--') followed by a new line ('\n')"),
      label.new(r"Replaces space character (' ') with plus ('+')"),
      label.new(r"Replaces space character (' ') with a random blank character from a valid set of alternate characters"),
      label.new(r"Replaces PostgreSQL SUBSTRING with LEFT and RIGHT"),
      label.new(r"Replaces AND and OR logical operators with their symbolic counterparts (&& and ||)"),
      label.new(r"Replaces instances of UNION ALL SELECT with UNION SELECT counterpart"),
      label.new(r"Replaces quote character (') with a multi-byte combo %BF%27 together with generic comment at the end (to make it work)"),
      label.new(r"Replaces each keyword character with upper case value (e.g. select -> SELECT)"),
      label.new(r"Appends a HTTP header 'X-originating-IP' to bypass Varnish Firewall"),
      label.new(r"Encloses each non-function keyword with (MySQL) versioned comment"),
      label.new(r"Encloses each keyword with (MySQL) versioned comment"),
      label.new(r"Append a fake HTTP header 'X-Forwarded-For' (and alike)"),
    ]

  def _(self, s):
    return s


def main():
  pass


if __name__ == '__main__':
  main()
