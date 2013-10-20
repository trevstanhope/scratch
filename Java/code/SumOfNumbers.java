import java.awt.*;
import java.sql.*;
import javax.swing.*;
import java.awt.event.*;
class SumOfNumbers{

    public static void main(String[] args){
    JFrame f=new JFrame();
    JLabel label1=new JLabel("First Number: ");
    JLabel label2=new JLabel("Second Number: ");
    JLabel label3=new JLabel("Result: ");
    final JTextField text1=new JTextField(20);
    final JTextField text2=new JTextField(20);
    final JTextField text3=new JTextField(20);
    JButton button=new JButton("Calculate");
    try{
           Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
           Connection con = DriverManager.getConnection("jdbc:odbc:student");
           Statement st=con.createStatement();
           ResultSet rs=st.executeQuery("select * from student where id=1");
           int mar1=0,mar2=0;
           if(rs.next()){
               mar1=rs.getInt("marks1");
               mar2=rs.getInt("marks2");
           }
           text1.setText(Integer.toString(mar1));
           text2.setText(Integer.toString(mar2));
           button.addActionListener(new ActionListener(){
               public void actionPerformed(ActionEvent e){
               int num1=Integer.parseInt(text1.getText());
               int num2=Integer.parseInt(text2.getText());
               int result=num1+num2;
               text3.setText(Integer.toString(result));
               }
            });
        }
        catch(Exception e){
        }
        JPanel p=new JPanel(new GridLayout(4,2));
        p.add(label1);
        p.add(text1);
        p.add(label2);
        p.add(text2);
        f.pack();
    }
}
