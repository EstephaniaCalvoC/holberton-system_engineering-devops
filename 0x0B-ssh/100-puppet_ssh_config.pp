# Configurate SSH to connect to a server without typing a password.

file_line { 'Turn off passwd auth':
  path     => '/etc/ssh/ssh_config',
  line     => 'PasswordAuthentication yes',
  match    => '#   PasswordAuthentication yes',
}

file_line { 'JuanMa':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}
