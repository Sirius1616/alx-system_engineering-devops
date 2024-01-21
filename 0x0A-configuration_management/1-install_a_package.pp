#!/usr/bin/pup
#Installing a package on puppet
package {'flask':
	ensure    => '2.1.0',
	providder => 'pip3',

}
