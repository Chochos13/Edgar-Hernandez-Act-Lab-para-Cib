param(  
    [string]$ResultFile="ParametrosIPPublica.txt",
    [string]$ResultFile1="ParametrosIPPrivada.txt",
    [string]$ResultFile2="ResultadosNmapSegmentoRed.txt",
    [string]$ResultFile3="ResultadosNmapScanme.nmap.org.txt",
    [string]$ResultFile4="ResultadosNmapIPpublica.txt"
)
$a = nmap 192.168.1.67 | Select-Object $a | Format-Table -HideTableHeaders | Out-File $ResultFile2 -Encoding ascii
$b = nmap scanme.nmap.org -Pn | Select-Object $b | Format-Table -HideTableHeaders | Out-File $ResultFile3 -Encoding ascii
$c = nmap 189.153.22.88 -Pn | Select-Object $c | Format-Table -HideTableHeaders | Out-File $ResultFile4 -Encoding ascii
$i = ipconfig | Select-Object $i | Format-Table -HideTableHeaders | Out-File $ResultFile1 -Encoding ascii
$j = (curl ifconfig.me).content | Select-Object $j | Format-Table -HideTableHeaders | Out-File $ResultFile -Encoding ascii

