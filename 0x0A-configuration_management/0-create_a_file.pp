# A puppet that creates a file with file path
file {'/tmp/school':
    content => 'I love Puppet\n',
    owner => 'www-data',
    group => 'www-data',
    mode => '0744',
}
