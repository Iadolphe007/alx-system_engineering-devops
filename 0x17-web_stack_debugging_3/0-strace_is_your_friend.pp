# fixing and automating puppet

exec { 'replace_line':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin','/usr/bin']
}
