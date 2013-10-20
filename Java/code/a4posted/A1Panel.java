package a4posted;
// Trevor Stanhope
// 260399515
// Due December 2nd, 2012

// Import Statements
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class A1Panel extends JPanel implements ActionListener{
        /*
        firstField = new JTextField("0", 10);
	    firstField.addActionListener(this);
	    secondField = new JTextField("0", 10);
	    secondField.addActionListener(this);
	    String text = textField.getText();
	    textArea.append(text + newline);
	    textField.selectAll();
        JFrame frame = new JFrame("TextDemo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(new TextDemo());
        frame.pack();
        frame.setVisible(true);
        */
        
	JButton calculate;
	JField firstField;
	JField secondField;
	JLabel result;

	TwoButtonPanel() {
		makeComponents();
		makeLayout();
	}

	private void makeComponents(){

		firstField = new JField("0", 10);
		firstField.addActionListener(this);

		secondField = new JField("button 2 (press me)");
		secondField.addActionListener(this);

        result = new JLabel();
		result.setFont(new Font("Times", Font.BOLD, 16));
		result.setBackground(Color.lightGray);
		result.setOpaque(true);
		result.setHorizontalAlignment( SwingConstants.CENTER );
	}

	private void makeLayout(){
		setLayout( new GridLayout(2,2));
		add(firstField);	
		add(secondField);
		add(calculate);
		add(result);
	}

	public void actionPerformed(ActionEvent e) { 
		if (e.getSource() == cc){
			count1++;
			label1.setText(" pushes: " + count1);
		}
		else if (e.getSource() == button2){
			count2++;
			label2.setText(" pushes " + count2);
		}
	}
}
