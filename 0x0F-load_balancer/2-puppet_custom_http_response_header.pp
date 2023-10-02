# installin nginx with pupett
exec {'apt update':
command => '/usr/bin/apt update',
}
package { 'nginx':
ensure  => installed,
require => Exec[apt update],
}
file {'/var/www/html/index.html':
content =>'Hello world!',
require => Package['nginx'],
}
file { '/var/www/html/404.html':
content => "Ceci n'est pas une page"
require => Package['nginx'],
}
exec {'nginx':
ensure  => running,
require => Package['nginx'],
}
