using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SQLite;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp2
{
    public partial class Form1 : Form
    {
        private const string connectionString = "Data Source=library.db;Version=3;";
        private DataGridView dataGridViewBooks;
        private TabControl tabControl;

        public Form1()
        {
            InitializeComponent();
            InitializeDataGridView();
            InitializeTabControl();
            AddControlsToForm();
            LoadBooks();
        }

        private void InitializeDataGridView()
        {
            dataGridViewBooks = new DataGridView();
            dataGridViewBooks.Dock = DockStyle.Fill;
            dataGridViewBooks.ReadOnly = true;
        }

        private void InitializeTabControl()
        {
            tabControl = new TabControl();
            tabControl.Dock = DockStyle.Fill;

            // Create and add the sign-in tab
            TabPage signInTab = new TabPage("Sign In");
            signInTab.Controls.Add(CreateSignInPanel());
            tabControl.TabPages.Add(signInTab);

            // Create and add the admin tab
            TabPage adminTab = new TabPage("Admin");
            adminTab.Controls.Add(CreateAdminPanel());
            tabControl.TabPages.Add(adminTab);

            // Create and add the user tab
            TabPage userTab = new TabPage("User");
            userTab.Controls.Add(CreateUserPanel());
            tabControl.TabPages.Add(userTab);
        }

        private Panel CreateSignInPanel()
        {
            Panel panel = new Panel();
            panel.Dock = DockStyle.Fill;

            // Add sign-in controls
            Label lblUsername = new Label();
            lblUsername.Text = "Username:";
            lblUsername.Location = new Point(50, 50);

            TextBox txtUsername = new TextBox();
            txtUsername.Location = new Point(150, 50);

            Label lblPassword = new Label();
            lblPassword.Text = "Password:";
            lblPassword.Location = new Point(50, 100);

            TextBox txtPassword = new TextBox();
            txtPassword.Location = new Point(150, 100);
            txtPassword.PasswordChar = '*';

            Button btnSignIn = new Button();
            btnSignIn.Text = "Sign In";
            btnSignIn.Location = new Point(150, 150);
            btnSignIn.Click += BtnSignIn_Click;

            panel.Controls.Add(lblUsername);
            panel.Controls.Add(txtUsername);
            panel.Controls.Add(lblPassword);
            panel.Controls.Add(txtPassword);
            panel.Controls.Add(btnSignIn);

            return panel;
        }

        private Panel CreateAdminPanel()
        {
            Panel panel = new Panel();
            panel.Dock = DockStyle.Fill;

            // Add admin controls
            Label lblAdminTitle = new Label();
            lblAdminTitle.Text = "Admin Screen";
            lblAdminTitle.Location = new Point(50, 50);

            // Add more controls for admin functionalities

            panel.Controls.Add(lblAdminTitle);

            return panel;
        }

        private Panel CreateUserPanel()
        {
            Panel panel = new Panel();
            panel.Dock = DockStyle.Fill;

            // Add user controls
            Label lblUserTitle = new Label();
            lblUserTitle.Text = "User Screen";
            lblUserTitle.Location = new Point(50, 50);

            // Add more controls for user functionalities

            panel.Controls.Add(lblUserTitle);

            return panel;
        }

        private void AddControlsToForm()
        {
            this.Controls.Add(tabControl);
        }

        private void LoadBooks()
        {
            dataGridViewBooks.DataSource = GetBooks();
        }

        private DataTable GetBooks()
        {
            DataTable dataTable = new DataTable();

            using (SQLiteConnection connection = new SQLiteConnection(connectionString))
            {
                connection.Open();

                string query = "SELECT * FROM Books";
                using (SQLiteCommand command = new SQLiteCommand(query, connection))
                {
                    using (SQLiteDataAdapter adapter = new SQLiteDataAdapter(command))
                    {
                        adapter.Fill(dataTable);
                    }
                }
            }

            return dataTable;
        }

        private void BtnSignIn_Click(object sender, EventArgs e)
        {
            // Perform authentication logic here
            // Check username and password against authorized admins and users

            // Example logic
            bool isAdmin = true; // Set to true for admin access, false for user access

            if (isAdmin)
            {
                tabControl.SelectedTab = tabControl.TabPages["Admin"];
            }
            else
            {
                tabControl.SelectedTab = tabControl.TabPages["User"];
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Code for loading books and other initialization
        }
    }
}
