#manifest that kills a process
# the process is named kill me now

exec {'killmenow':
command  => '/usr/bin/pkill killmenow',
provider => 'shell',
returns  => [0,1],
}
