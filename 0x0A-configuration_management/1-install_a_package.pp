# Puppet Manifest to Install Flask with pip3

# Ensure the directory exists
file { '/tmp':
  ensure => directory,
}

# Install Flask using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => File['/tmp'],  # Ensure the directory exists before installing
}
