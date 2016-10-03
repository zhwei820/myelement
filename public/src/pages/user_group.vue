<template lang="html">

<div class="">

      <el-breadcrumb separator="/">
        <el-breadcrumb-item>首页</el-breadcrumb-item>
        <el-breadcrumb-item>设置</el-breadcrumb-item>
        <el-breadcrumb-item>管理员分组管理</el-breadcrumb-item>
      </el-breadcrumb>


      <el-form :inline="true" :model="formInline" class="demo-form-inline">
        <el-form-item>
          <el-button type="primary" @click.native.prevent="onCreate">新建</el-button>
        </el-form-item>

      </el-form>

      <el-dialog title="" v-model="dialogFormVisible">

          <el-form :model="userGroupForm" ref="userGroupForm" label-width="100px" >
            <el-form-item label="分组名称" prop="email">
              <el-input v-model="userGroupForm.name"></el-input>
            </el-form-item>

              <el-input type="hidden" v-model="userGroupForm.id"></el-input>

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
            property="id"
            label="ID"
            >
        </el-table-column>
        <el-table-column
            property="name"
            label="名称"
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
      userGroupForm: {
        name: '',
        id: '',
      },
      rules: {
        name: [
          { required: true, message: '请输入分组名称', trigger: 'change' }
        ],

      },
      formInline: {
        name: '',
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
      this.$refs.userGroupForm.resetFields();
    },
    handleSubmit(ev) {
      this.$refs.userGroupForm.validate((valid) => {
        if (valid) {
          console.log(this.userGroupForm);
          var res;
          if(this.userGroupForm.id > 0){
            res = this.$http.put('/ends/a_user/get_user_group/', this.userGroupForm)
          }else {
            res = this.$http.post('/ends/a_user/get_user_group/', this.userGroupForm)
          }
          res.then((response) => {
            if(response.data.status > 0){
              this.error_message = response.data.message;
            }else {
              this.onSearch();
            }
          });
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    onSearch(ev) {
      this.$http.get('/ends/a_user/get_user_group/', {params: this.formInline}).then((response) => {
        if(response.data.status > 0){
          this.error_message = response.data.message;
        }else {
          this._tableData = response.data;
          if(this._tableData[0]){
            this.total_page = this._tableData.length
            this.tableData = this._tableData.slice(0, this.per_page)
          }
        }
      });
    },
    cellClick(row, column, cell, event){
      var button_text = event.toElement.innerText;
      if(button_text == '编辑'){
        this.dialogFormVisible = true;
        this.userGroupForm = {
          name: row.name,
          id: row.id,
        };
      }else if(button_text == '上架') {

      }else if (button_text == '下架') {

      }
    },
    onCreate(){
      this.dialogFormVisible = true;
      this.userGroupForm = {
        name: '',
        id: '',
      };
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
