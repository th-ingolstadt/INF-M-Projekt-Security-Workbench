<head>
<title>Denial of Service Example</title>
</head>

<body>
<h1>Denial of Service Example</h1>

<?php

function multiply_matrix($m1, $m2)
{

	if(is_array($m1) && is_array($m2))
	{

		$m1_rows = count($m1);
		$m1_cols = count($m1[0]);
		$m2_rows = count($m2);
		$m2_cols = count($m2[0]);

		$result_rows = $m1_rows;
		$result_cols = $m2_cols;

		$result = array();

		if($m1_cols != $m2_rows)
		{
			echo "Matrizen-Dimensionen passen nicht!";
		}
		else
		{
			for($i=0; $i < $m1_rows; $i++)
			{
				for($j=0; $j < $m2_cols; $j++)
				{
					$result[$i][$j] = 0;
					for($k=0; $k < $m2_rows; $k++)
					{
						$result[$i][$j] += $m1[$i][$k] * $m2[$k][$j];
					}
				}
			}
		}
	}
	else
	{
		echo "Matrixmultiplikation: Matrizen müssen als Array übergeben werden!";
	}
	
	return $result;
}

$m1 = Array(
	Array(1, 2),
	Array(3, 4)
);
$m2 = Array(
	Array(1, 2),
	Array(3, 4)
);

$result = multiply_matrix($m1, $m2);

print_r($result);

?>

</body>

