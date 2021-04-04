# Configurate SSH to connect to a server without typing a password.

include stdlib

file_line { 'Turn off passwd auth':
  path =>  '/etc/ssh/ssh_config',
  line =>  'PasswordAuthentication no',
}

file_line {  'Declare identity file':
  path =>  '/etc/ssh/ssh_config',
  line =>  'IdentityFile ~/.ssh/holberton',
}
