import paramiko

def get_sftp():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('localhost', username='root', password='B4nan-purr(en)')
    return client

def test2():
    client = get_sftp()
    sftp = client.open_sftp()
    sftp.stat('/tmp')
    sftp.close()


if __name__ == "__main__":
    test2()
    
    sftp_client = get_sftp()
    
    sftp_client = ssh_client.open_sftp()
    
    remote_file = sftp_client.open('remote_filename')
    try:
	for line in remote_file:
	    # process line
    finally:
	remote_file.close()
    