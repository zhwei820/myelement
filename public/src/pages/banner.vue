<template lang="html">

<div class="">

      <el-breadcrumb separator="/">
        <el-breadcrumb-item>首页</el-breadcrumb-item>
        <el-breadcrumb-item>运营</el-breadcrumb-item>
        <el-breadcrumb-item>banner管理</el-breadcrumb-item>
      </el-breadcrumb>

      <el-form :inline="true" :model="formInline" @click.native.prevent="onSearch" class="demo-form-inline">
        <el-form-item >
          <el-input v-model="formInline.user" placeholder="审批人"></el-input>
        </el-form-item>
        <el-form-item>
          <el-select v-model="formInline.region" placeholder="活动区域">
            <el-option label="区域一" value="shanghai"></el-option>
            <el-option label="区域二" value="beijing"></el-option>
          </el-select>
        </el-form-item>

        <el-form-item>

          <div class="block">
            <span class="demonstration">起止日期</span>
            <el-date-picker
              v-model="formInline.date_range"
              type="daterange"
              align="right"
              placeholder="选择日期范围"
              :picker-options="pickerOptions2"
              style="width: 220px">
            </el-date-picker>
          </div>
        </el-form-item>

        <el-form-item>
          <el-button type="primary">查询</el-button>
        </el-form-item>
      </el-form>

      <el-dialog title="收货地址" v-model="dialogFormVisible">

          <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
            <el-form-item label="活动名称" prop="name">
              <el-input v-model="ruleForm.name"></el-input>
            </el-form-item>
            <el-form-item label="活动区域" prop="region">
              <el-select v-model="ruleForm.region" placeholder="请选择活动区域">
                <el-option label="区域一" value="shanghai"></el-option>
                <el-option label="区域二" value="beijing"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="活动时间">

              <el-date-picker
                v-model="ruleForm.date1"
                type="datetime"
                placeholder="选择日期时间">
              </el-date-picker>
            </el-form-item>
            <el-form-item label="即时配送">
              <el-switch on-text="" off-text="" v-model="ruleForm.delivery"></el-switch>
            </el-form-item>
            <el-form-item label="活动性质" prop="type">
              <el-checkbox-group v-model="ruleForm.type">
                <el-checkbox label="美食/餐厅线上活动" name="type"></el-checkbox>
                <el-checkbox label="地推活动" name="type"></el-checkbox>
                <el-checkbox label="线下主题活动" name="type"></el-checkbox>
                <el-checkbox label="单纯品牌曝光" name="type"></el-checkbox>
              </el-checkbox-group>
            </el-form-item>
            <el-form-item label="特殊资源" prop="resource">
              <el-radio-group v-model="ruleForm.resource">
                <el-radio label="线上品牌商赞助"></el-radio>
                <el-radio label="线下场地免费"></el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item label="活动形式" prop="desc">
              <el-input type="textarea" v-model="ruleForm.desc"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click.native.prevent="handleSubmit">立即创建</el-button>
              <el-button @click.native.prevent="handleReset">重置</el-button>
            </el-form-item>
          </el-form>

        <span slot="footer" class="dialog-footer">
          <el-button @click.native="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click.native="dialogFormVisible = false">确 定</el-button>
        </span>
      </el-dialog>


      <el-table
        :data="tableData"
        @cellclick="cellClick"
        border
        style="width: 100%">

        <el-table-column
            inline-template
            label="操作"
            width="180"
            >
            <el-button-group>
                <el-button type="primary" size="small">编辑</el-button>
                <el-button type="primary" size="small">上架</el-button>
                <el-button type="primary" size="small">下架</el-button>
            </el-button-group>
        </el-table-column>
        <el-table-column
            property="date"
            label="日期"
            width="180">
        </el-table-column>
        <el-table-column
            property="name"
            label="姓名"
            width="180">
        </el-table-column>
        <el-table-column
            property="address"
            label="地址"
        </el-table-column>

      </el-table>

      <div class="">
        <el-pagination
          @sizechange="handleSizeChange"
          @currentchange="handleCurrentChange"
          :current-page="5"
          :page-sizes="[100, 200, 300, 400]"
          :page-size="100"
          layout="total, sizes, prev, pager, next, jumper"
          :total="400">
        </el-pagination>
      </div>

</div>

</template>

<script>

export default {
  data () {
    return {
      dialogFormVisible: false,
      formLabelWidth: '40',
      tableData: [{
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-08',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-06',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-07',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }],

      ruleForm: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },
      rules: {
        name: [
          { required: true, message: '请输入活动名称', trigger: 'blur' }
        ],
        region: [
          { required: true, message: '请选择活动区域', trigger: 'change' }
        ],
        date1: [
          { type: 'date', required: true, message: '请选择日期', trigger: 'change' }
        ],
        date2: [
          { type: 'date', required: true, message: '请选择时间', trigger: 'change' }
        ],
        type: [
          { type: 'array', required: true, message: '请至少选择一个活动性质', trigger: 'change' }
        ],
        resource: [
          { required: true, message: '请选择活动资源', trigger: 'change' }
        ],
        desc: [
          { required: true, message: '请填写活动形式', trigger: 'blur' }
        ]
      },
      formInline: {
        user: '',
        region: '',
        date_range: '',
      },

      pickerOptions2: {
         shortcuts: [{
           text: '最近一周',
           onClick(picker) {
             const end = new Date();
             const start = new Date();
             start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
             picker.$emit('pick', [start, end]);
           }
         }, {
           text: '最近一个月',
           onClick(picker) {
             const end = new Date();
             const start = new Date();
             start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
             picker.$emit('pick', [start, end]);
           }
         }, {
           text: '最近三个月',
           onClick(picker) {
             const end = new Date();
             const start = new Date();
             start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
             picker.$emit('pick', [start, end]);
           }
         }]
       },

    }
  },
  computed: {},
  ready () {},
  attached () {},
  methods: {

    handleReset() {
      this.$refs.ruleForm.resetFields();
    },
    handleSubmit(ev) {
      this.$refs.ruleForm.validate((valid) => {
        if (valid) {
          alert('submit!');
          console.log(this.ruleForm);

        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    onSearch(ev) {
      console.log('submit!');
      console.log(this.formInline);
    },
    cellClick(row, column, cell, event){
      var button_text = event.toElement.innerText;
      if(button_text == '编辑'){
        console.log(button_text);
      }else if(button_text == '上架') {
        console.log(button_text);
      }else if (button_text == '下架') {
        console.log(button_text);
        console.log();
        this.dialogFormVisible = true;

        this.ruleForm = {
          name: '来来来来来来',
          region: 'shanghai',
          date1: '2016-05-05',
          date2: '2016-05-05',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        };
      }
    },
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
    },
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
    },
  },
  components: {

  }
};
</script>

<style lang="css">
</style>
