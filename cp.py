#!/usr/bin/env python
"""
Usage:
    cp.py [backup] [restore] [copy]


This will only remote file source
"""

import os
import sys
import shutil
import logging
try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve

logger = logging.getLogger()


def get_file_names():
    s = """
    apkd_launcher_air_au_com_metro_DumbWaysToDie-air_au_com_metro_DumbWaysToDie_AppEntry.png
    apkd_launcher_air_com_RustyLake_CubeEscapeTheMill_wdj-com_pujia8_start.png
    apkd_launcher_air_com_gamebrain_twelve-air_com_gamebrain_twelve_AppEntry.png
    apkd_launcher_air_com_globz_lampvamp-air_com_globz_lampvamp_AppEntry.png
    apkd_launcher_air_com_wacha_pixelfodderlite-air_com_wacha_pixelfodderlite_AppEntry.png
    apkd_launcher_air_z3lf_five5-air_z3lf_five5_AppEntry.png
    apkd_launcher_cn_amazon_mShop_android-com_amazon_mShop_splashscreen_StartupActivity.png
    apkd_launcher_cn_com_open_mooc-com_mooc_imooc_ui_loading_MCLoadingActivity.png
    apkd_launcher_cn_goapk_market-cn_goapk_market_GoApkLoginAndRegister.png
    apkd_launcher_cn_ibuka_manga_ui-cn_ibuka_manga_ui_ActivityStartup.png
    apkd_launcher_cn_konami_contraevo-org_ksh_contra_contra__android.png
    apkd_launcher_cn_kuwo_player-cn_kuwo_player_activities_EntryActivity.png
    apkd_launcher_cn_lm_sq-cn_lm_sq_Sq.png
    apkd_launcher_cn_tagux_myshare-cn_tagux_myshare_MainActivity.png
    apkd_launcher_cn_wiz_note-cn_wiz_note_MainActivity.png
    apkd_launcher_cn_wps_moffice__eng-cn_wps_moffice_documentmanager_PreStartActivity.png
    apkd_launcher_com_DuckyGames_SaveThePuck-com_unity3d_player_UnityPlayerProxyActivity.png
    apkd_launcher_com_FranticEyes_Catch-com_unity3d_player_UnityPlayerActivity.png
    apkd_launcher_com_Moanbej_Astrosurf-com_unity3d_player_UnityPlayerProxyActivity.png
    apkd_launcher_com_MobileTicket-com_MobileTicket_MobileTicket.png
    apkd_launcher_com_NVS_gogogrow-com_unity3d_player_UnityPlayerProxyActivity.png
    apkd_launcher_com_SuperAwesome_Stop-com_unity3d_player_UnityPlayerNativeActivity.png
    apkd_launcher_com_UCMobile-com_UCMobile_main_UCMobile.png
    apkd_launcher_com_UCMobile_intl-com_UCMobile_main_UCMobile.png
    apkd_launcher_com_adobe_reader-com_adobe_reader_AdobeReader.png
    apkd_launcher_com_alcomi_toiletdefense-com_alcomi_toiletdefense_DemoActivity.png
    apkd_launcher_com_alibaba_mobileim-com_alibaba_mobileim_SplashActivity.png
    apkd_launcher_com_amazon_kindle-com_amazon_kindle_UpgradePage.png
    apkd_launcher_com_android_bankabc-com_android_bankabc_LPSplash.png
    apkd_launcher_com_android_bankabc-com_android_bankabc_MainActivity.png
    apkd_launcher_com_animoca_google_robo5-muneris_android_unity_Activity.png
    apkd_launcher_com_aptoide_partners-com_aptoide_partners_StartPartner.png
    apkd_launcher_com_autonavi_minimap-com_autonavi_map_activity_SplashActivity.png
    apkd_launcher_com_autonavi_minimap-com_autonavi_minimap_Splashy.png
    apkd_launcher_com_baidu_BaiduMap-com_baidu_baidumaps_WelcomeScreen.png
    apkd_launcher_com_baidu_netdisk-com_baidu_netdisk_ui_Navigate.png
    apkd_launcher_com_baozou_baozou_android-com_baozou_baozou_android_MainActivity.png
    apkd_launcher_com_baozou_baozou_android-com_baozou_baozoudaily_LauncherActivity.png
    apkd_launcher_com_baozoumanhua_android-com_baozoumanhua_android_LoadActivity.png
    apkd_launcher_com_bulkypix_iamabraveknight-com_unity3d_player_UnityPlayerNativeActivity.png
    apkd_launcher_com_carrot_carrotfantasy-com_carrot_carrotfantasy_CarrotFantasy.png
    apkd_launcher_com_carrot_iceworld-com_carrot_iceworld_CarrotFantasy.png
    apkd_launcher_com_chinamworld_main-com_ccb_mbs_main_StartActivity.png
    apkd_launcher_com_cyh_framed-com_cyh_ui_SplashUI.png
    apkd_launcher_com_disney_stackrabbit__goo-com_disney_matchstacker_MatchStackerActivity.png
    apkd_launcher_com_disney_wheresmywater2__goo-com_disney_wheresmywater2__goo_ActivitySkuGoogle.png
    apkd_launcher_com_douban_radio-com_douban_radio_ui_WelcomeActivity.png
    apkd_launcher_com_eg_android_AlipayGphone-com_eg_android_AlipayGphone_AlipayLogin.png
    apkd_launcher_com_enfeel_birzzle-com_enfeel_birzzle_Birzzle.png
    apkd_launcher_com_ezinterweb_weseewey-com_giderosmobile_android_weseeweActivity.png
    apkd_launcher_com_facebook_katana-com_facebook_nodex_startup_splashscreen_NodexSplashActivity.png
    apkd_launcher_com_feelingtouch_dipan_slggameglobal-com_dipan_platform_FirstPage.png
    apkd_launcher_com_flypig_PopTile-com_flypig_PopTile_PopTile.png
    apkd_launcher_com_gameloft_android_ANMP_GloftD3HM-com_inject_InjectActivity.png
    apkd_launcher_com_gameloft_android_ANMP_GloftDMCN-com_gameloft_android_ANMP_GloftDMCN_Game.png
    apkd_launcher_com_gameloft_android_ANMP_GloftDMHM-com_gameloft_android_ANMP_GloftDMHM_Game.png
    apkd_launcher_com_gameloft_android_ANMPwdj_GloftD4HC-com_gameloft_android_ANMPwdj_GloftD4HC_Game.png
    apkd_launcher_com_gewara-com_gewara_main_CoverActivity.png
    apkd_launcher_com_gramgames_ten0ten0-com_unity3d_player_UnityPlayerNativeActivity.png
    apkd_launcher_com_greenpoint_android_mc10086_activity-com_greenpoint_android_mc10086_activity_StartPageActivity.png
    apkd_launcher_com_grupoalamar_people-com_grupoalamar_people_RunnerActivity.png
    apkd_launcher_com_guokr_android-com_guokr_android_guokrcollection_ui_activity_WelcomeActivity.png
    apkd_launcher_com_halfbrick_jetpackjoyride-com_halfbrick_mortar_MortarGameActivityFacebook.png
    apkd_launcher_com_halfbrick_jetpackjoyridepaid-com_skynet_android_impl_ui_SkynetSplashActivity.png
    apkd_launcher_com_headupgames_bridgeconstructormedieval-com_prime31_UnityPlayerProxyActivity.png
    apkd_launcher_com_hftp_dumbway-com_hftp_dumbway_DumbwayActivity.png
    apkd_launcher_com_hlinapp_drawcal-com_pzw_framework_PluginContainer.png
    apkd_launcher_com_hostelworld_app-com_hostelworld_app_controller_ExploreActivity.png
    apkd_launcher_com_imangi_templerun-com_templerun1_SkyNetPluginActivity.png
    apkd_launcher_com_imangi_templerun2-com_skynet_android_impl_ui_SkynetSplashActivity.png
    apkd_launcher_com_instagram_android-com_instagram_android_activity_MainTabActivity.png
    apkd_launcher_com_ipeaksoft_kengbeng-com_ipeaksoft_kengbeng_SplashActivity.png
    apkd_launcher_com_jsplash_savemypixel-com_unity3d_player_UnityPlayerProxyActivity.png
    apkd_launcher_com_ketchapp_jellyjump-com_ketchapp_jellyjump_UnityPlayerNativeActivity.png
    apkd_launcher_com_ketchapp_stickhero-com_ketchapp_stickhero_stickhero.png
    apkd_launcher_com_king_candycrushsaga-com_king_candycrushsaga_CandyCrushSagaActivity.png
    apkd_launcher_com_kingsoft-com_kingsoft_StartActivity.png
    apkd_launcher_com_kugou_android-com_kugou_android_app_splash_SplashActivity.png
    apkd_launcher_com_lima_doodlejump-com_limasky_doodlejumpandroid_MainActivity.png
    apkd_launcher_com_linker_hfyt-com_linker_hfyt_StartActivity01.png
    apkd_launcher_com_meiriyiwen_app-com_meiriyiwen_app_________________________.png
    apkd_launcher_com_microsoft_office_onenote-com_microsoft_office_onenote_ui_ONMSplashActivity.png
    apkd_launcher_com_microsoft_rdc_android-com_microsoft_rdc_ui_activities_HomeActivity.png
    apkd_launcher_com_microsoft_skydrive-com_microsoft_skydrive_MainActivity.png
    apkd_launcher_com_mudloop_adam-com_androidnative_AndroidNativeBridge.png
    apkd_launcher_com_naver_linewebtoon-com_naver_linewebtoon_splash_SplashActivity.png
    apkd_launcher_com_nitrome_sillysausage-com_nitrome_sillysausage_Main.png
    apkd_launcher_com_nobstudio_bloodrun-com_ansca_corona_CoronaActivity.png
    apkd_launcher_com_noodlecake_anothercasesolved-com_noodlecake_anothercasesolved_AnotherCaseSolved.png
    apkd_launcher_com_noodlecake_rsb-com_apportable_activity_VerdeActivity.png
    apkd_launcher_com_noshufou_android_su-com_noshufou_android_su_HomeActivity.png
    apkd_launcher_com_oliverpearl_slydrsfree-com_oliverpearl_slydrsfree_Main.png
    apkd_launcher_com_outerminds_tadpoletap-com_unity3d_player_UnityPlayerNativeActivity.png
    apkd_launcher_com_pikpok_gbod-com_pikpok_gbod_GBODActivity.png
    apkd_launcher_com_popcap_pvz2cthd360-com_popcap_SexyApp_SexyAppActivity.png
    apkd_launcher_com_popcap_pvz2cthdwdj-com_popcap_pvz2cthdwdj_SexyAppActivity.png
    apkd_launcher_com_quora_android-com_quora_android_LauncherActivity.png
    apkd_launcher_com_qzone-com_tencent_sc_activity_SplashActivity.png
    apkd_launcher_com_realarcade_DOJ-com_realarcade_DOJ_MrGame.png
    apkd_launcher_com_rebeltwins_aliensdrivemecrazy-com_prime31_UnityPlayerNativeActivity.png
    apkd_launcher_com_rebeltwins_daddywasathief-com_prime31_UnityPlayerNativeActivity.png
    apkd_launcher_com_rinzz_noonedies-com_rinzz_noonedies_MainActivity.png
    apkd_launcher_com_ripstone_mrm-com_ripstone_mrm_MRM.png
    apkd_launcher_com_rovio_amazingalex_free-com_rovio_amazingalex_AAActivity.png
    apkd_launcher_com_rovio_amazingalex_koooopesf34k-com_rovio_amazingalex_AAActivity.png
    apkd_launcher_com_rovio_angrybirdsstarwars_ads_iap-com_rovio_fusion_App.png
    apkd_launcher_com_rovio_angrybirdsstella-com_rovio_fusion_App.png
    apkd_launcher_com_sainthyler_muffin-com_tivicloud_ui_SplashActivity.png
    apkd_launcher_com_slipcorp_microtrip-com_slipcorp_microtrip_Microtrip.png
    apkd_launcher_com_taobao_appcenter-com_taobao_ui_WelcomeActivity.png
    apkd_launcher_com_taobao_taobao-com_taobao_tao_Welcome.png
    apkd_launcher_com_taobao_taobao-com_taobao_tao_welcome_Welcome.png
    apkd_launcher_com_ted_android-com_ted_android_view_activity_SplashScreenActivity.png
    apkd_launcher_com_tencent_androidqqmail-com_tencent_qqmail_LaucherActivity.png
    apkd_launcher_com_tencent_mm-com_tencent_mm_ui_LauncherUI.png
    apkd_launcher_com_tencent_mobileqqi-com_tencent_mobileqq_activity_SplashActivity.png
    apkd_launcher_com_tencent_pb-com_tencent_pb_launch_PhoneBookActivity.png
    apkd_launcher_com_thankcreate_EasyAdventure-com_thankcreate_EasyAdventure_EasyAdventure.png
    apkd_launcher_com_thankcreate_NormalAdventure-com_thankcreate_NormalAdventure_NormalAdventure.png
    apkd_launcher_com_thankcreate_StrangeAdventure-com_thankcreate_StrangeAdventure_StrangeAdventure.png
    apkd_launcher_com_tudou_android-com_tudou_ui_activity_WelcomeActivity.png
    apkd_launcher_com_tumblr-com_tumblr_ui_activity_JumpoffActivity.png
    apkd_launcher_com_tuokio_smashtheschool-com_prime31_UnityPlayerNativeActivity.png
    apkd_launcher_com_twitter_android-com_twitter_android_StartActivity.png
    apkd_launcher_com_twodboy_worldofgoofull-com_twodboy_worldofgoofull_WorldOfGooFull.png
    apkd_launcher_com_u17_comic_phone-com_u17_phone_ui_FirstActivity.png
    apkd_launcher_com_ubercab-com_ubercab_client_feature_launch_LauncherActivity.png
    apkd_launcher_com_uc_browser_en-com_uc_browser_ActivityBrowser.png
    apkd_launcher_com_usaya_TubeCat-com_usaya_TubeCat_TubeCat.png
    apkd_launcher_com_ustwo_monumentvalleycnnc-com_ustwo_deviceutil_MainActivity.png
    apkd_launcher_com_veewo_darkslash-com_veewo_darkslash_defaultAct.png
    apkd_launcher_com_venbrux_tntbf2-com_venbrux_tntbf2_RunnerActivity.png
    apkd_launcher_com_venbrux_tntbf3-com_venbrux_tntbf3_RunnerActivity.png
    apkd_launcher_com_wandoujia_phoenix2-com_wandoujia_jupiter_activity_HomeActivity.png
    apkd_launcher_com_wandoujia_phoenix2-com_wandoujia_p4_activity_ExploreActivity.png
    apkd_launcher_com_wapple_neonfigure-com_wapple_neonfigure_RunnerActivity.png
    apkd_launcher_com_warnerbros_game300ROE-com_prime31_UnityPlayerNativeActivity.png
    apkd_launcher_com_xunlei_downloadprovider-com_xunlei_downloadprovider_loading_LoadingActivity.png
    apkd_launcher_com_yandex_store-com_yandex_store_MainActivity.png
    apkd_launcher_com_youdao_dict-com_youdao_dict_activity_DictSplashActivity.png
    apkd_launcher_com_youku_phone-com_youku_phone_ActivityWelcome.png
    apkd_launcher_com_ytm_game_colorblock-org_cocos2dx_cpp_AppActivity.png
    apkd_launcher_com_yyf_PhysicsPaper-com_unity3d_player_UnityPlayerProxyActivity.png
    apkd_launcher_com_zeptolab_ctr2_f2p_google-com_zeptolab_ctr2_CTR2Activity.png
    apkd_launcher_com_zhihu_android-com_zhihu_android_ui_activity_GuideActivity.png
    apkd_launcher_com_zhihu_circlely_android-com_zhihu_circlely_android_activity_SplashActivity__.png
    apkd_launcher_com_zhihu_daily_android-com_zhihu_daily_android_activity_GuideActivity__.png
    apkd_launcher_com_zhihu_daily_android-com_zhihu_daily_android_activity_SplashActivity__.png
    apkd_launcher_doudoufight_passwordstorm-doudoufight_passwordstorm_FlashActivity.png
    apkd_launcher_fm_qingting_qtradio-fm_qingting_qtradio_QTRadioActivity.png
    apkd_launcher_fm_xiami_main-fm_xiami_bmamba_activity_StartMainActivity.png
    apkd_launcher_fm_xiami_main-fm_xiami_main_SplashActivity.png
    apkd_launcher_jamgame_absorb_wdj-org_cocos2dx_cpp_AppActivity.png
    apkd_launcher_jp_co_capcom_android_bio4__LGUplus0119-com_inject_InjectActivity.png
    apkd_launcher_kb_Blek-com_unity3d_player_UnityPlayerNativeActivity.png
    apkd_launcher_net_oschina_app-net_oschina_app_AppStart.png
    apkd_launcher_net_oschina_gitapp-net_oschina_gitapp_WelcomePage.png
    apkd_launcher_org_coursera_android-org_coursera_android_MainActivity.png
    apkd_launcher_org_fdroid_fdroid-org_fdroid_fdroid_FDroid.png
    apkd_launcher_org_mozilla_firefox-org_mozilla_gecko_BrowserApp.png
    apkd_launcher_org_videolan_vlc_betav7neon-org_videolan_vlc_betav7neon_gui_MainActivity.png
    apkd_launcher_ppl_unity_JuiceCubesBeta-com_prime31_UnityPlayerProxyActivity.png
    apkd_launcher_team_deepdarkdeveloper_billy-com_unity3d_player_UnityPlayerProxyActivity.png
    apkd_launcher_tv_danmaku_bili-tv_danmaku_bili_LauncherActivity.png
    apkd_launcher_tv_danmaku_bili-tv_danmaku_bili_ui_splash_SplashActivity.png
    apkd_launcher_ua_krou_memory-ua_krou_memory_activities_GameMenuActivity.png
    apkd_launcher_yong_universalplayer-com_hd_video_player_ui_MainActivity.png
    """

    return (x.strip() for x in s.strip().splitlines())


def get_url(name):
    return (('https://raw.githubusercontent.com/TylerTemp/'
             'DroidSailizedIcon/master/apkd/') + name)


def get_local(name):
    return '/var/lib/apkd/' + name


def backup():
    total = failed = 0
    for name in get_file_names():
        local_file = get_local(name)
        if os.path.exists(local_file):
            pref, file = os.path.split(local_file)
            backup_file = os.path.join(pref, '.' + file)
            total += 1
            if not _replace(local_file, backup_file):
                failed += 1
                logger.error('backup failed %s', common)

    if failed != 0:
        logger.error('backup complete %s/%s', total - failed, total)
    else:
        logger.info('backup complete')


def restore():
    total = failed = 0
    local_folder = get_local('')
    _, _, files = next(os.walk(local_folder))

    for dotfile in (x for x in files if x.startswith('.')):
        total += 1

        old = os.path.join(local_folder, docfile)
        new = os.path.join(local_folder, docfile[1:])

        if not _replace(old, new):
            failed += 1
            logger.error('restore failed %s', docopt)

    if failed != 0:
        logger.error('restore complete %s/%s', total - failed, total)
    else:
        logger.info('restore complete')


def copy():
    total = 0
    failed = []
    for name in get_file_names():
        local_file = get_local(name)
        if os.path.exists(local_file):
            total += 1
            url = get_url(name)
            logger.debug('%s: %s', local_file, url)
            try:
                f, _ = urlretrieve(url, local_file)
            except BaseException as e:
                failed.append(name)
                logger.error(e)
            else:
                logger.info(f)


    if failed:
        logger.error('copy complete %s/%s', total - len(failed), total)
        logger.error(failed)
    else:
        logger.info('copy complete')


def _replace(old, new):
    try:
        shutil.copy2(old, new)
    except BaseException as e:
        logger.error('replace %s failed: %s', old, e)
        return False
    else:
        logger.debug('replace %s finished', old)
        return True


if __name__ == '__main__':
    formatter = logging.Formatter('\033[32m%(levelname)1.1s\033[0m '
                                  '%(lineno)3d %(funcName)s | %(message)s')
    hdlr = logging.StreamHandler(sys.stdout)
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)

    if len(sys.argv) == 1:
        sys.argv.extend(('backup', 'copy'))

    for each in sys.argv[1:]:
        if each == 'backup':
            backup()
        elif each == 'restore':
            restore()
        elif each == 'copy':
            copy()
        else:
            logger.error('unknown argv %s', each)
