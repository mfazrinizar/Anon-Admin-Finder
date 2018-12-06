#! /usr/bin/python

import httplib,socket,sys
import subprocess as me
import optparse

if sys.platform == 'linux' or sys.platform == 'linux2':
	me.call("clear",shell=True)
else:
	me.call("cls",shell=True)


anon="""
\t\t+=================================================+
\t\t+      Creator  : Anon6372098                     +
\t\t+      Contact  : anon6372098.id@gmail.com        +                             
\t\t+      Team     : D4RK SYST3M F41LUR3 S33K3R      +
\t\t+      Homepage : https://www.dsfs-indo.zone.id/  +                                       
\t\t+      Thanks to: All Member of DSFS Official     +       
\t\t+=================================================+"""

parser=optparse.OptionParser(usage='python2 %s  -t http://target.domain' %(sys.argv[0]))
parser.add_option("-t", action="store",dest="target",help="target site", default="")

(options,args) = parser.parse_args()
if options.target=="": 
	print (anon)
	print ("Type \"python2 %s -h\" for help"%sys.argv[0])
else:

	try:
		var1=0
		var2=0
	
		php = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
		'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
		'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
		'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
		'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
		'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
		'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
		'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
		'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
		'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
		'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
		'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
		'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
		'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
		'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
		'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
		'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
		'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
		'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','/adminpanel','user.php','account.html','controlpanel.html','admincontrol.html','panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','adminarea/index.php','adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php','modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php','adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']
	
		try:
			print (anon)
			alamat=options.target		#raw_input("Masukkan Alamat Target : ")
			alamat=alamat.replace("http://","")
			print ("Check " + alamat + " dulu.Harap tunggu...")
			konek=httplib.HTTPConnection(alamat)
			konek.connect()
			print "[A] Bagus + Target Online + Bagus\n"
		except (httplib.HTTPResponse, socket.error) as Exit:
			raw_input("[S] Sepertinya, server offline atau alamat target salah")
			exit()
		#print "Masukkan site source"
		#print "1. PHP (default)"
		angka=1 #input("> ")
			
		if angka == 1:
			print "\t[A] Scanning " + alamat + "...."
			i=0
			for admin in php:
				admin=admin.replace("\n","")
				admin="/" + admin
				host=alamat + admin
				print ("\t[W] Cek " + alamat + "/"+ php[i] + "...")
				koneksi=httplib.HTTPConnection(alamat)
				koneksi.request("GET",admin)
				respon=koneksi.getresponse()
				var2=var2+1
				i=i+1
				if respon.status==200:
					var1=var1+1
					print "%s %s" % ( "\n\n>>>" + host, "Admin page/halaman admin ditemukan !")
	        	    		raw_input("Tekan enter untuk melanjutkan.\n")
	        		elif respon.status == 404:
	        	    		var2 = var2
	        		elif respon.status == 302:
	        	    		print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
	        		else:
	        	    		print "%s %s %s" % (host, " Interesting response:", respon.status)
	        	    		koneksi.close()
			print("\n\nSelesai!!! \n")
		        print var1, " Halaman admin ditemukan"
	        	print var2, " Total halaman scanned"
	        	raw_input("[/] Selesai; Tekan enter untuk keluar")		
	

	except (httplib.HTTPResponse, socket.error):
		print "\n\t[S] Sesi dibatalkan; Terdapat error. Cek koneksi/pengaturan internet !"
	except (KeyboardInterrupt, SystemExit):
		print "\n\t[S] Sesi dibatalkan"
	except:
                print "\n\t[S] Error Tidak Diketahui, Exit !"