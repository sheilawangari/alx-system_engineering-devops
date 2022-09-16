# Create a file named holberton in tmp with owner and group www-data
file {'/tmp/holberton':
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  mode    => '0744',
}
