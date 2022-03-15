param(  
    [string]$ResultFile="Resultados.txt",
    [string]$ResultFile1="Resultados1.txt",
    [string]$ResultFile2="Resultados2.txt"
)

$status = (Invoke-WebRequest https://docs.zerotier.com/openapi/centralv1.json).StatusCode
$statusdes = (Invoke-WebRequest https://docs.zerotier.com/openapi/centralv1.json).StatusDescription
if ( ($status = 200) -and ($statusdes = "OK"))
{
	$j = (Invoke-WebRequest https://docs.zerotier.com/openapi/centralv1.json).content | Select-Object $j | Format-Table -HideTableHeaders | Out-File $ResultFile -Encoding ascii
	$s = (Invoke-WebRequest https://docs.zerotier.com/openapi/centralv1.json).Rawcontent | Select-Object $s | Format-Table -HideTableHeaders | Out-File $ResultFile1 -Encoding ascii
	$k = Invoke-RestMethod https://docs.zerotier.com/openapi/centralv1.json -Method GET | Select-Object $k | Format-Table -HideTableHeaders | Out-File $ResultFile2 -Encoding ascii
}
