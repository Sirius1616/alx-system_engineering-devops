#Installing a package on puppet
package {'flask':
	ensure    => '2.1.0',
	provider => 'pip3',

}