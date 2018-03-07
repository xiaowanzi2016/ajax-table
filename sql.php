<?php
	class Mysql{
		public $db_server;
		public $db_user;
		public $db_pass;
		public $db_db;

		function _construct(){
			$this->$db_server="localhost";
			$this->$db_user="root";
			$this->$db_pass="123456";
			$this->$db_db="doubantop250";
			$this->link= $this->dbConnect();
		}
		function dbConnect(){
			$link=mysqli_connect("localhost","root","123456","doubantop250");
			if(!$link)
				{
					die('Could not connect: ' . mysqli_connect_error());
				}
			else 
				return $link;
		}
		function dbQuery($strSql){
			return @mysqli_query($this->link,$strSql);
		}
		
	}
	class Store{
		public $id;
		public $name;
		public $ranking;
		public $score;
		public $score_num;
		function _construct(){
		$this->$id=array();
		$this->$name=array();
		$this->$ranking=array();
		$this->$score=array();
		$this->$score_num=array();
        }
    }
	
?>