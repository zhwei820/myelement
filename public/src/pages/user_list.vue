<template lang="html">

<div class="">

      <el-breadcrumb separator="/">
        <el-breadcrumb-item>首页</el-breadcrumb-item>
        <el-breadcrumb-item>设置</el-breadcrumb-item>
        <el-breadcrumb-item>管理员管理</el-breadcrumb-item>
      </el-breadcrumb>

      <el-form :inline="true" :model="formInline" class="demo-form-inline">
        <el-form-item >
          <el-input v-model="formInline.user" placeholder="管理员"></el-input>
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
              :picker-options="pickerOptions"
              style="width: 220px">
            </el-date-picker>
          </div>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click.native.prevent="onSearch">查询</el-button>
        </el-form-item>
      </el-form>

      <el-dialog title="" v-model="dialogFormVisible">

          <el-form :model="adminUserForm" :rules="rules" ref="adminUserForm" label-width="100px" class="demo-adminUserForm">
            <el-form-item label="账号" prop="email">
              <el-input v-model="adminUserForm.email"></el-input>
            </el-form-item>
            <el-form-item label="活动区域" prop="region">
              <el-select v-model="adminUserForm.region" placeholder="请选择活动区域">
                <el-option label="区域一" value="shanghai"></el-option>
                <el-option label="区域二" value="beijing"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="加入时间">
              <el-date-picker
                v-model="adminUserForm.ctime"
                type="datetime"
                placeholder="选择日期时间">
              </el-date-picker>
            </el-form-item>
            <el-form-item label="有效">
              <el-switch on-text="" off-text="" v-model="adminUserForm.delivery"></el-switch>
            </el-form-item>
            <el-form-item label="用户tag" prop="type">
              <el-checkbox-group v-model="adminUserForm.type">
                <el-checkbox label="美食/餐厅线上活动" name="type"></el-checkbox>
                <el-checkbox label="地推活动" name="type"></el-checkbox>
                <el-checkbox label="线下主题活动" name="type"></el-checkbox>
                <el-checkbox label="单纯品牌曝光" name="type"></el-checkbox>
              </el-checkbox-group>
            </el-form-item>
            <el-form-item label="特殊资源" prop="resource">
              <el-radio-group v-model="adminUserForm.resource">
                <el-radio label="线上品牌商赞助"></el-radio>
                <el-radio label="线下场地免费"></el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item label="活动textarea" prop="desc">
              <el-input type="textarea" v-model="adminUserForm.desc"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click.native.prevent="handleSubmit">创建</el-button>
              <el-button @click.native.prevent="handleReset">重置</el-button>
            </el-form-item>
          </el-form>

      </el-dialog>

      <el-table
        :data="tableData"
        @cellclick="cellClick"
        border
        style="width: 100%">

        <el-table-column
            inline-template
            label="操作"
            >
            <el-button-group>
                <el-button type="primary" size="small">编辑</el-button>
                <el-button type="primary" size="small">上架</el-button>
                <el-button type="primary" size="small">下架</el-button>
            </el-button-group>
        </el-table-column>
        <el-table-column
            property="email"
            label="账号"
            >
        </el-table-column>
        <el-table-column
            property="username"
            label="用户名"
            >
        </el-table-column>
        <el-table-column
            property="__is_superuser"
            label="是否超级管理员"
            >
        </el-table-column>
        <el-table-column
            property="date_joined"
            label="加入日期"
        </el-table-column>
        <el-table-column
            property="last_login"
            label="最后登录日期"
            >
        </el-table-column>
      </el-table>

      <div class="">
        <el-pagination
          @sizechange="handleSizeChange"
          @currentchange="handleCurrentChange"
          :current-page="current_page"
          :page-sizes="[1, 100, 200, 300, 400]"
          :page-size="per_page"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total_page">
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
      tableData: [],
      adminUserForm: {
        name: '',
        region: '',
        ctime: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },
      rules: {
        email: [
          { required: true, message: '请输入活动名称', trigger: 'blur' }
        ],
        region: [
          { required: true, message: '请选择活动区域', trigger: 'change' }
        ],
        ctime: [
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

      pickerOptions: {
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
       current_page: 1,
       total_page: 1,
       per_page: 100,

    }
  },
  computed: {},
  mounted () {
    this.onSearch();
  },
  attached () {},
  methods: {
    handleReset() {
      this.$refs.adminUserForm.resetFields();
    },
    handleSubmit(ev) {
      this.$refs.adminUserForm.validate((valid) => {
        if (valid) {
          alert('submit!');
          console.log(this.adminUserForm);
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    onSearch(ev) {
      this.$http.get('/ends/a_user/a_user_list/', {params: this.formInline}).then((response) => {
        if(response.data.status > 0){
          this.error_message = response.data.message;
        }else {
          console.log(response.data);
          this._tableData = response.data;
          this.total_page = this._tableData.length
          this.tableData = this._tableData.slice(0, this.per_page)
        }
      });
    },
    cellClick(row, column, cell, event){
      var button_text = event.toElement.innerText;
      if(button_text == '编辑'){
        this.dialogFormVisible = true;

        this.adminUserForm = {
          email: 'zw@mysite.com',
          region: 'shanghai',
          delivery: false,
          ctime: '2016-05-05',
          type: [],
          resource: '',
          desc: ''
        };

      }else if(button_text == '上架') {

      }else if (button_text == '下架') {

      }
    },
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
      this.per_page = val;
      if(this._tableData){
        this.tableData = this._tableData.slice(this.per_page * (this.current_page - 1), this.per_page * this.current_page);
      }
    },
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      this.current_page = val;
      if(this._tableData){
        this.tableData = this._tableData.slice(this.per_page * (this.current_page - 1), this.per_page * this.current_page);
      }
    },
  },
  components: {

  }
};
</script>

<style lang="css">
</style>
