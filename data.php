<?php
	require_once("./sql.php");
	$page=$_POST['page'];//获得传递过来的页码
	//每页显示的数量
	$showcount=5;
	$store=new Store();
	$i=0;
	if($page==1)
		{$startPage=0;}
	else
		{$startPage=($page-1)*5+1;}
	$mysql=new Mysql();
	$link=$mysql->dbConnect();
	mysqli_query($link,"set names 'utf8'");
	
	$sql="select * from doubantop250 limit $startPage, $showcount";
	$result=mysqli_query($link,$sql);
	while($row=mysqli_fetch_array($result)){
			
			$store->id[$i]=$row[0];
			$store->name[$i]=$row[1];
			$store->ranking[$i]=$row[2];
			$store->score[$i]=$row[3];
			$store->score_num[$i]=$row[4];
		    $i++;
	}
    echo json_encode($store);
?>