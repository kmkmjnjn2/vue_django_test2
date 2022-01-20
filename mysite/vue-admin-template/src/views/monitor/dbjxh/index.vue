<template>
    <div class="dashboard-editor-container">
      <div class="header">
        <h1>地板机械化</h1>

      </div>


<!--      <div class="dbjxh-table el-row">-->
<!--          <el-table :data="M_info"  border :header-cell-style="{textAlign: 'center',background: '#f5f7fa'}" :cell-style="{ textAlign: 'center' }" style="width:100% ;margin: auto ;">-->
<!--            <el-table-column prop="line" label="生产线" ></el-table-column>-->
<!--            <el-table-column prop="车型1现存" label="车型1现存" ></el-table-column>-->
<!--            <el-table-column prop="车型2现存" label="车型2现存" ></el-table-column>-->
<!--            <el-table-column prop="车型3现存" label="车型3现存" ></el-table-column>-->
<!--            <el-table-column prop="满位报警" label="满位报警" ></el-table-column>-->
<!--            <el-table-column prop="预满位报警" label="预满位报警" ></el-table-column>-->
<!--            <el-table-column prop="车型1限制数" label="车型1限制数" ></el-table-column>-->
<!--            <el-table-column prop="车型2限制数" label="车型2限制数" ></el-table-column>-->
<!--            <el-table-column prop="车型3限制数" label="车型3限制数" ></el-table-column>-->
<!--            <el-table-column prop="车型1已上线数" label="车型1已上线数" ></el-table-column>-->
<!--            <el-table-column prop="车型2已上线数" label="车型2已上线数" ></el-table-column>-->
<!--            <el-table-column prop="车型3已上线数" label="车型3已上线数" ></el-table-column>-->
<!--            <el-table-column prop="现存总数" label="现存总数" ></el-table-column>-->
<!--            <el-table-column prop="上线数" label="上线数" ></el-table-column>-->
<!--          </el-table>-->
<!--      </div>-->





      <el-card shadow="always" class="box-card" :body-style="{ height: '100%' }" style="padding: 16px;margin-bottom: 15px">

          <table>
            <tr style="height: 20%;">
              <th  style="border-bottom: none;"  >
                <img src="../../../icons/svg/hongqi.png" alt="">
              </th>
              <th colspan="3" style="background-color: #8fbc8b">M1</th>
              <th colspan="3" style="background-color: #bdb76b">M2</th>
              <th colspan="3" style="background-color: #00ced1">M3</th>
            </tr>
            <tr style="height: 15%;">
              <th  style="border-top: none">{{datetime | formaDate}}</th>
              <th style="width: 8%">HS5</th>
              <th style="width: 8%">E111</th>
              <th style="width: 8%">J71</th>
              <th style="width: 8%">H5</th>
              <th style="width: 8%">HS5</th>
              <th style="width: 8%;background-color:#dcdcdc">预留</th>
              <th style="width: 8%">H5</th>
              <th style="width: 8%">HS5</th>
              <th style="width: 8%;background-color:#dcdcdc">预留</th>
            </tr>
            <tr style="height: 10%;">
              <th >现存数</th>
<!--              M1现存数-->
              <th>{{Line_dist['LCD1_M1.车型1现存']}}</th>
              <th>{{Line_dist['LCD1_M1.车型2现存']}}</th>
              <th>{{Line_dist['LCD1_M1.车型3现存']}}</th>
<!--              M2现存数-->
              <th>{{Line_dist['LCD1_M2.车型1现存']}}</th>
              <th>{{Line_dist['LCD1_M2.车型2现存']}}</th>
              <th style="background-color:#dcdcdc ">{{Line_dist['LCD1_M2.车型3现存']}}</th>
<!--              M3现存数-->
              <th>{{Line_dist['LCD1_M3.车型1现存']}}</th>
              <th>{{Line_dist['LCD1_M3.车型2现存']}}</th>
              <th style="background-color:#dcdcdc ">{{Line_dist['LCD1_M3.车型3现存']}}</th>
            </tr>
            <tr style="height: 10%;">

              <th>限制数</th>
<!--              M1限制数-->
              <th>{{Line_dist['LCD1_M1.车型1限制数']}}</th>
              <th>{{Line_dist['LCD1_M1.车型2限制数']}}</th>
              <th>{{Line_dist['LCD1_M1.车型3限制数']}}</th>
<!--              M2限制数-->
              <th>{{Line_dist['LCD1_M2.车型1限制数']}}</th>
              <th>{{Line_dist['LCD1_M2.车型2限制数']}}</th>
              <th style="background-color:#dcdcdc ">{{Line_dist['LCD1_M2.车型3限制数']}}</th>
<!--              M3限制数-->
              <th>{{Line_dist['LCD1_M3.车型1限制数']}}</th>
              <th>{{Line_dist['LCD1_M3.车型2限制数']}}</th>
              <th style="background-color:#dcdcdc ">{{Line_dist['LCD1_M3.车型3限制数']}}</th>
            </tr>

            <tr style="height: 10%;">
              <th>已上线</th>
<!--              M1已上线数-->
              <th>{{Line_dist['LCD1_M1.车型1已上线数']}}</th>
              <th>{{Line_dist['LCD1_M1.车型2已上线数']}}</th>
              <th>{{Line_dist['LCD1_M1.车型3已上线数']}}</th>
<!--              M2已上线数-->
              <th>{{Line_dist['LCD1_M2.车型1已上线数']}}</th>
              <th>{{Line_dist['LCD1_M2.车型2已上线数']}}</th>
              <th style="background-color:#dcdcdc ">{{Line_dist['LCD1_M2.车型3已上线数']}}</th>
<!--              M3已上线数-->
              <th>{{Line_dist['LCD1_M3.车型1已上线数']}}</th>
              <th>{{Line_dist['LCD1_M3.车型2已上线数']}}</th>
              <th style="background-color:#dcdcdc ">{{Line_dist['LCD1_M3.车型3已上线数']}}</th>
            </tr>
            <tr style="height: 10%;">
              <th>现存总数</th>
              <th colspan="3">{{Line_dist['LCD1_M1.现存总数']}}</th>
              <th colspan="3">{{Line_dist['LCD1_M2.现存总数']}}</th>
              <th colspan="3">{{Line_dist['LCD1_M3.现存总数']}}</th>
            </tr>
            <tr style="height: 10%;">
              <th>上线数</th>
              <th colspan="3">{{Line_dist['LCD1_M1.上线数']}}</th>
              <th colspan="3">{{Line_dist['LCD1_M2.上线数']}}</th>
              <th colspan="3">{{Line_dist['LCD1_M3.上线数']}}</th>
            </tr>
            <tr style="height: 10%;">
              <th>上线总数</th>
              <th colspan="4">{{Line_dist['LCD1_上线总数']}}</th>
              <th>下线总数</th>
              <th colspan="4">{{Line_dist['LCD1_下线总数']}}</th>
            </tr>

          </table>


      </el-card>






      <div style="display: flex;justify-content: space-between">
      <el-card shadow="always" class="box-card2" :body-style="{ height: '100%' }" style="padding: 16px;margin-bottom: 15px">

        <table>
          <tr>
            <th colspan="4" style="height: 10%;background-color: rgb(143, 188, 139)">M1</th>
          </tr>
          <tr style="height: 5%">
            <th>序号</th>
            <th>位置</th>
            <th>车型</th>
            <th>流水号</th>
          </tr>
          <tr v-for="(value , name , index) in M1_Car_Style_dist">
            <td>{{index+1}}</td>
            <td>{{name}}</td>
            <td>{{value}}</td>
            <td>{{M1_LSH_dist[name]}}</td>
          </tr>
        </table>

      </el-card>

      <el-card shadow="always" class="box-card3" :body-style="{ height: '100%' }" style="padding: 16px;margin-bottom: 15px">
        <table>
          <tr>
            <th colspan="4" style="height: 10%;background-color: rgb(189, 183, 107)">M2</th>
          </tr>
          <tr style="height: 5%">
            <th>序号</th>
            <th>位置</th>
            <th>车型</th>
            <th>流水号</th>
          </tr>
          <tr v-for="(value , name , index) in M2_Car_Style_dist">
            <td>{{index+1}}</td>
            <td>{{name}}</td>
            <td>{{value}}</td>
            <td>{{M2_LSH_dist[name]}}</td>
          </tr>
        </table>
      </el-card>

        <el-card shadow="always" class="box-card4" :body-style="{ height: '100%' }" style="padding: 16px;margin-bottom: 15px">
        <table>
          <tr>
            <th colspan="4"style="height: 10%;background-color: rgb(0, 206, 209)">M3</th>
          </tr>
          <tr style="height: 5%">
            <th>序号</th>
            <th>位置</th>
            <th>车型</th>
            <th>流水号</th>
          </tr>
          <tr v-for="(value , name , index) in M3_Car_Style_dist">
            <td>{{index+1}}</td>
            <td>{{name}}</td>
            <td>{{value}}</td>
            <td>{{M3_LSH_dist[name]}}</td>
          </tr>
        </table>
      </el-card>

      </div>







<!--      <div>-->
<!--        <h1>分割</h1>-->
<!--      </div>-->

<!--     <div>-->
<!--      <button @click="BtnBooks">点击返回booklist列表</button>-->
<!--      <h3 v-for="book in Books">-->
<!--        id是：{{book.id}}-->
<!--        书名是：{{book.btitle}}-->
<!--        上传日期是：{{book.bpub_data}}-->
<!--      </h3>-->
<!--    </div>-->

<!--      <div>-->
<!--        <button @click="BtnLine">点击返回地板机械化信息列表</button>-->
<!--        <h3 v-for="info in Line_Info">-->
<!--        id是：{{info.id}}-->
<!--        线体是：{{info.line}}-->
<!--        名称是：{{info.name}}-->
<!--        上传日期是：{{info.value}}-->
<!--      </h3>-->


<!--      </div>-->


    </div>
</template>

<script>
  import axios from 'axios'

    export default {
        name: "index",
      data(){
          return{
            msg:0,
            datetime:new Date(),
            tableData: [
              {
                date: '2016-05-02',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1518 弄'
              }, {
                date: '2016-05-04',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1517 弄'
              }, {
                date: '2016-05-01',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1519 弄'
              }, {
                date: '2016-05-03',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1516 弄'
              }
            ],
            Books:[],
            Line_Info:[],
            value_info:[],
            M_info:[],
            Line_dist:{},
            M1_Car_Style_dist:{},
            M1_LSH_dist:{},
            M2_Car_Style_dist:{},
            M2_LSH_dist:{},
            M3_Car_Style_dist:{},
            M3_LSH_dist:{},



          }
      },
      watch:{

          value_info:{
            handler(newvalue,oldvalue){
              console.log("new_value:",newvalue)
              console.log("old_value:",oldvalue)
            },

          },


      },

      methods:{
        showmsg(){
          this.msg=123

        },
        BtnBooks:function () {
          axios.post('http://localhost/api/Books')
          .then((response)=>{
            console.log('response is :',response)
            console.log('response.data is ',response.data)
            this.Books=response.data

          })

        },
        BtnLine:function () {
          axios.post('http://47.94.218.39/api/Line')
          .then((response)=>{
            console.log('response is :',response)
            console.log('response.data is ',response.data)
            this.Line_Info=response.data
            console.log('this.Line_Info is ',this.Line_Info)
            console.log("this.Line_Info的类型是",typeof(this.Line_Info))
            console.log("this.Line_Info[0]的类型是",typeof(this.Line_Info[0]))
            console.log("this.Line_Info[0]",this.Line_Info[0].value)
            this.value_info=[]
            this.M_info=[]
            for(var line_info of this.Line_Info){
                this.Line_dist[line_info.name]=line_info.value
                if (line_info.name.search("M1_Car_Style") != -1){

                  this.M1_Car_Style_dist[line_info.name.split(".")[2]]=line_info.value
                }
                if (line_info.name.search("M1_LSH") != -1){

                  this.M1_LSH_dist[line_info.name.split(".")[2]]=(line_info.value > 999 ?  line_info.value : line_info.value > 0? "0"+line_info.value:0)
                }
                if (line_info.name.search("M2_Car_Style") != -1){

                  this.M2_Car_Style_dist[line_info.name.split(".")[2]]=line_info.value
                }
                if (line_info.name.search("M2_LSH") != -1){

                  this.M2_LSH_dist[line_info.name.split(".")[2]]=(line_info.value > 999 ?  line_info.value : line_info.value > 0? "0"+line_info.value:0)
                }
                if (line_info.name.search("M3_Car_Style") != -1){

                  this.M3_Car_Style_dist[line_info.name.split(".")[2]]=line_info.value
                }
                if (line_info.name.search("M3_LSH") != -1){

                  this.M3_LSH_dist[line_info.name.split(".")[2]]=(line_info.value > 999 ?  line_info.value : line_info.value > 0? "0"+line_info.value:0)
                }

            }
            console.log("this.Line_dist的内容是：",this.Line_dist)
            console.log("M1_Car_Style_dist的内容是：",this.M1_Car_Style_dist)
            console.log("M1_LSH的内容是：",this.M1_LSH_dist)
          })

        },





      },
      mounted() {
        let that = this
        that.BtnLine()

        this.timer2 = setInterval(function () {
          that.datetime = new Date();
        },1000);
         this.timer = setInterval(function(){
          that.BtnLine()
           console.log("BtnLine已经执行")
        }, 5000);




      },
      beforeDestroy() {
          clearInterval(this.timer)
          clearInterval(this.timer2)
      },
      filters:{

          formaDate:function (value) {
            let that = this
            var date = new Date()
            var year = date.getFullYear()
            var month = date.getMonth()+1
            var day = date.getDate()<10?'0'+date.getDate():date.getDate()
            var hours = date.getHours()<10?'0'+date.getHours():date.getHours()
            var minutes = date.getMinutes()<10?'0'+date.getMinutes():date.getMinutes()
            var seconds = date.getSeconds()<10?'0'+date.getSeconds():date.getSeconds()
            return(
               year+
                "-"+
              month+
              "-"  +
              day  +
              "   "+
              hours+
              ":"+
              minutes+
              ":"+
              seconds
            )

          }
      }

    }
</script>

<style scoped>
  .dashboard-editor-container{
    background-color:rgb(240,242,245) ;
    position: relative;
    padding: 15px;
  }

  tr {
    /*border: 1px solid #909399;*/

  }
  th{
    /*background: #f5f7fa;*/
    display: table-cell;
    border:1px solid grey;
    border-collapse: separate;
    border-spacing: 2px;
  }
  td{
    display: table-cell;
    border:1px solid grey;
    border-collapse: separate;
    border-spacing: 2px;

  }




  table{
    width: 100%;
    height: 100%;
    border: 2px solid black;
    border-collapse: collapse;
    border-spacing: 2px;
    padding: 1px;
    /*border-bottom: none;*/
    font-size: 25px;
  }

  .dbjxh-table{
    /*box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);*/
    background:rgb(255,255,255);
    padding: 16px 16px ;
    margin-bottom: 32px;
  }

  el-table-column{
    text-Align: center;

  }
  .el-table{
    font-size: 14px;
    color: #606266;

  }

  .header{
    position: center;
    text-align: center;
    color:#303133;
    /*color:#409EFF;*/
  }


  .text {
    font-size: 14px;
  }

  .item {
    padding: 18px 0;
  }

  .box-card {
    width: 100%;
    padding: 1px;
    border: 2px;
    border-color: grey;
    height: 60vh;
  }

  .box-card2 {
    width: 30%;
    padding: 1px;
    border: 2px;
    border-color: grey;
    height: 90vh;
    text-align: center;

  }

   .box-card3 {
    width: 30%;
    padding: 1px;
    border: 2px;
    border-color: grey;
    height: 90vh;
    text-align: center;

  }
  .box-card4 {
    width: 30%;
    padding: 1px;
    border: 2px;
    border-color: grey;
    height: 90vh;
    text-align: center;

  }



</style>
