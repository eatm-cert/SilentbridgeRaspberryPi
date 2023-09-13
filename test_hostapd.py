from core.hostapd import Hostapd
import core.core_config
import settings.paths

if __name__ == '__main__':
	hostapd_conf = core.core_config.CoreConfig(settings.paths.HOSTAPD_INI, settings.paths.HOSTAPD_CONF)
#	hostapd_conf.update('cli', 'interface', 'eth1')
	hostapd_conf.write()

	hostapd = Hostapd(hostapd_conf.hostapd_conf_path)
	hostapd.start()

	raw_input('Press any key')
	
	hostapd.stop()
