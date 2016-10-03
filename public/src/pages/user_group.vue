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

      <el-dialog title="分组管理" v-model="dialogFormVisible">

          <el-form :model="userGroupForm" ref="userGroupForm" label-width="100px" >
            <el-form-item label="分组名称" prop="email">
              <el-input v-model="userGroupForm.name"></el-input>
            </el-form-item>

              <el-input type="hidden" v-model="userGroupForm.id"></el-input>

              <el-button type="primary" @click.native.prevent="handleSubmit">提交</el-button>
              <el-button @click.native.prevent="handleReset">重置</el-button>
            </el-form-item>
          </el-form>

      </el-dialog>

      <el-dialog title="分组成员" v-model="groupUserFormVisible">

          <el-form :model="groupUserForm" ref="groupUserForm" label-width="100px" >
            <el-form-item label="分组名称" prop="email">
              <el-input v-model="groupUserForm.name"></el-input>
            </el-form-item>

            <el-form-item label="用户" prop="type">
              <el-checkbox-group v-model="groupUserForm.user_id">
                <el-checkbox :label="user.id" name="user_id" v-for="user in groupUserForm.users">{{ user.name }}</el-checkbox>
              </el-checkbox-group>
            </el-form-item>

              <el-input type="hidden" v-model="groupUserForm.id"></el-input>

              <el-button type="primary" @click.native.prevent="handleSubmit">提交</el-button>
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
                <el-button type="primary" size="small">查看/编辑成员</el-button>
                <el-button type="primary" size="small">查看/编辑权限</el-button>
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
      groupUserFormVisible: false,
      formLabelWidth: '40',
      tableData: [],
      userGroupForm: {
        name: '',
        id: 0,
      },
      groupUserForm: {
        name: '',
        users: [],
        user_id: [],
      },
      user_list: [{'name': 'zw', 'id': 1, 'group_id': 1},],
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
              this.dialogFormVisible = false;
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
      }else if(button_text == '查看/编辑成员') {
        this.groupUserFormVisible = true;
        this.$http.get('/ends/a_user/get_user_group_detail/', {params: {'id': row.id}}).then((response) => {
          if(response.data.status > 0){
            this.error_message = response.data.message;
          }else {
            this.groupUserForm = {
              name: row.name,
              id: row.id,
              users: response.data,
              user_id: [],
            };
            for (var i = 0; i < this.groupUserForm.users.length; i++) {
              if(this.groupUserForm.users['group_id'] == row.id){
                this.groupUserForm.user_id.push(this.groupUserForm.users['id']);
              }
            }
          }
        });
      }else if (button_text == '下架') {

      }
    },
    onCreate(){
      this.dialogFormVisible = true;
      this.userGroupForm = {
        name: '',
        id: 0,
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
