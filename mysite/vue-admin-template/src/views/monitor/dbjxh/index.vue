<template>
    <div class="dashboard-editor-container">
      <div class="header">
        <h1>地板机械化数据</h1>

      </div>

<!--      <h1>地板机械化对应内容</h1>-->
<!--      <div class="dbjxh-table">-->
<!--          <el-table :data="tableData" border style="width:100% ;margin: auto" >-->
<!--            <el-table-column prop="date" label="日期" width="180"></el-table-column>-->
<!--            <el-table-column prop="name" label="姓名" width="180"></el-table-column>-->
<!--            <el-table-column prop="address" label="地址" width="100%"></el-table-column>-->
<!--          </el-table>-->
<!--      </div>-->

<!--      <div class="dbjxh-table">-->
<!--          <el-table  border :header-cell-style="{textAlign: 'center'}" :cell-style="{ textAlign: 'center' }" style="width:100% ;margin: auto ;">-->
<!--            <el-table-column label="存储区" ></el-table-column>-->
<!--            <el-table-column label="M1" aria-colspan="3"></el-table-column>-->
<!--            <el-table-column label="M2" aria-colspan="3"></el-table-column>-->
<!--            <el-table-column label="M3" aria-colspan="3"></el-table-column>-->
<!--          </el-table>-->
<!--      </div>-->


      <div class="dbjxh-table el-row">
          <el-table :data="M_info"  border :header-cell-style="{textAlign: 'center',background: '#f5f7fa'}" :cell-style="{ textAlign: 'center' }" style="width:100% ;margin: auto ;">
            <el-table-column prop="line" label="生产线" ></el-table-column>
            <el-table-column prop="车型1现存" label="车型1现存" ></el-table-column>
            <el-table-column prop="车型2现存" label="车型2现存" ></el-table-column>
            <el-table-column prop="车型3现存" label="车型3现存" ></el-table-column>
            <el-table-column prop="满位报警" label="满位报警" ></el-table-column>
            <el-table-column prop="预满位报警" label="预满位报警" ></el-table-column>
            <el-table-column prop="车型1限制数" label="车型1限制数" ></el-table-column>
            <el-table-column prop="车型2限制数" label="车型2限制数" ></el-table-column>
            <el-table-column prop="车型3限制数" label="车型3限制数" ></el-table-column>
            <el-table-column prop="车型1已上线数" label="车型1已上线数" ></el-table-column>
            <el-table-column prop="车型2已上线数" label="车型2已上线数" ></el-table-column>
            <el-table-column prop="车型3已上线数" label="车型3已上线数" ></el-table-column>
            <el-table-column prop="现存总数" label="现存总数" ></el-table-column>
            <el-table-column prop="上线数" label="上线数" ></el-table-column>
          </el-table>
      </div>







<!--      <div>-->
<!--        <table>-->
<!--          <tr>-->
<!--            <th>存储区</th>-->
<!--            <th colspan="3">M1</th>-->
<!--            <th colspan="3">M2</th>-->
<!--            <th colspan="3">M3</th>-->
<!--          </tr>-->
<!--          <tr>-->
<!--            <th>车型</th>-->
<!--            <th>HS5</th>-->
<!--            <th>E111</th>-->
<!--            <th>J71</th>-->
<!--            <th>H5</th>-->
<!--            <th>HS5</th>-->
<!--            <th>预留</th>-->
<!--            <th>H5</th>-->
<!--            <th>HS5</th>-->
<!--            <th>预留</th>-->
<!--          </tr>-->
<!--          <tr>-->
<!--            <th>现存数</th>-->
<!--            <th>{{value_info[0]}}</th>-->
<!--            <th>{{value_info[1]}}</th>-->
<!--            <th>{{value_info[2]}}</th>-->
<!--            <th>{{value_info[13]}}</th>-->
<!--            <th>{{value_info[14]}}</th>-->
<!--            <th>{{value_info[15]}}</th>-->
<!--            <th>{{value_info[26]}}</th>-->
<!--            <th>{{value_info[27]}}</th>-->
<!--            <th>{{value_info[28]}}</th>-->
<!--          </tr>-->
<!--          <tr>-->
<!--            <th>限制数</th>-->
<!--            <th>{{value_info[5]}}</th>-->
<!--            <th>{{value_info[6]}}</th>-->
<!--            <th>{{value_info[7]}}</th>-->
<!--            <th>{{value_info[18]}}</th>-->
<!--            <th>{{value_info[19]}}</th>-->
<!--            <th>{{value_info[20]}}</th>-->
<!--            <th>{{value_info[31]}}</th>-->
<!--            <th>{{value_info[32]}}</th>-->
<!--            <th>{{value_info[33]}}</th>-->
<!--          </tr>-->
<!--          <tr>-->
<!--            <th>已上线</th>-->
<!--            <th>{{value_info[8]}}</th>-->
<!--            <th>{{value_info[9]}}</th>-->
<!--            <th>{{value_info[10]}}</th>-->
<!--            <th>{{value_info[21]}}</th>-->
<!--            <th>{{value_info[22]}}</th>-->
<!--            <th>{{value_info[23]}}</th>-->
<!--            <th>{{value_info[34]}}</th>-->
<!--            <th>{{value_info[35]}}</th>-->
<!--            <th>{{value_info[36]}}</th>-->
<!--          </tr>-->
<!--          <tr>-->
<!--            <th>现存总数</th>-->
<!--            <th colspan="3">{{value_info[11]}}</th>-->
<!--            <th colspan="3">{{value_info[24]}}</th>-->
<!--            <th colspan="3">{{value_info[37]}}</th>-->
<!--          </tr>-->
<!--          <tr>-->
<!--            <th>上线数</th>-->
<!--            <th colspan="3">{{value_info[12]}}</th>-->
<!--            <th colspan="3">{{value_info[25]}}</th>-->
<!--            <th colspan="3">{{value_info[38]}}</th>-->
<!--          </tr>-->
<!--          <tr>-->
<!--            <th>上线总数</th>-->
<!--            <th colspan="4">{{value_info[39]}}</th>-->
<!--            <th>下线总数</th>-->
<!--            <th colspan="4">{{value_info[40]}}</th>-->
<!--          </tr>-->



<!--        </table>-->


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
          axios.post('http://localhost/api/Line')
          .then((response)=>{
            console.log('response is :',response)
            console.log('response.data is ',response.data)
            this.Line_Info=response.data
            console.log('this.Line_Info is ',this.Line_Info)
            console.log("this.Line_Info的类型是",typeof(this.Line_Info))
            console.log("this.Line_Info[0]的类型是",typeof(this.Line_Info[0]))
            console.log("this.Line_Info[0]",this.Line_Info[0].id)
            this.value_info=[]
            this.M_info=[]
            var dict={}
            for(var line_info of this.Line_Info  ){
              this.value_info.push(line_info.value)
              console.log("line_info is ",line_info)

              dict[line_info.name]=line_info.value
              dict['line']=line_info.line
              if(line_info.id==113 ||line_info.id==213 ||line_info.id==313){
                this.M_info.push(dict)
                dict={}
              }
            }
            console.log("M_info is",this.M_info)

          })

        },


      },
      mounted() {
        let that = this
        that.BtnLine()
         this.timer = setInterval(function(){
          that.BtnLine()
           console.log("BtnLine已经执行")
        }, 5000);

      },
      beforeDestroy() {
          clearInterval(this.timer)
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
  border: 1px solid #909399;
  }
  th{
    background: #f5f7fa;
  }
  table{
    width: 100%;
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








</style>
