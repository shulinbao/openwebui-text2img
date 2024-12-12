# openwebui-text2img
这个函数可以为openwebui添加文生图功能，并支持one-api格式的api传入

### 使用方法
1. 以管理员身份登录Openwebui，打开以下链接：
   `https://your-open-webui-url/admin/functions`
2. 添加一个新函数，将text2img.py中的代码拷贝进并保存
3. 点击右侧Valves，进行配置
   ![圖片](https://github.com/user-attachments/assets/dfc49350-6a23-442d-b6be-f8f4dda95b24)
4. 启用函数
   ![圖片](https://github.com/user-attachments/assets/32099f31-1e66-422b-be1a-bb60e5434191)
5. 新增一个模型，按照如下方式配置：
   ![圖片](https://github.com/user-attachments/assets/1f40bcf5-8c4a-49c8-b6f8-7886e1e2d75b)
   ![圖片](https://github.com/user-attachments/assets/2af9be3f-27cf-4198-8a33-c63ac6fe859a)
   一定要记得勾选Filters！提示词如下：
   ```
   You are a text-to-image prompt generator, and your task is to convert my words into English prompts. You should remove non-descriptive content from my sentences, for example: “Draw a sleeping kitten,” you only need to extract the main subject: “A sleeping kitten.” Then, translate them into English prompts, being sure to remain faithful to my original text.
   ```
6. 使用你新建的模型吧！效果如下：
   ![圖片](https://github.com/user-attachments/assets/be419e72-d033-4f47-84fd-572bd5ec3b58)
