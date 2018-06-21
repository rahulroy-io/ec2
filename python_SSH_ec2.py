import paramiko
key = paramiko.RSAKey.from_private_key_file("/temp/.pem")
con = paramiko.SSHClient()
con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
host = ''
con.connect( hostname = host, username = "ec2_user", pkey = key )

commands = [
        "pwd",
        "ls",
        "pwd"
        ]


for command in commands:
        print ("Executing {}".format(command))
        stdin , stdout, stderr = con.exec_command(command)
        print (stdout.read())
        print (stderr.read())
