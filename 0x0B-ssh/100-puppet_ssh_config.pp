# config file to connect without 
include stdlib
file_line  {'Declare identity file':
ensure   => 'present',
path     => '/etc/ssh/ssh_confing',
line     => '    IdentityFile ~/.ssh/school',
replace  => true,
}

file_line {'Turn off passwd auth':
ensure   => 'present',
path     => '/etc/ssh/ssh_config',
line     => '    PasswordAuthentication no',
replace  => true,
}
