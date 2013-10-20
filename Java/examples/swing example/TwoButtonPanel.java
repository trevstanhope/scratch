package swingDemos;

import java.awt.Color;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;

public class TwoButtonPanel extends JPanel implements ActionListener { 

	int count1 = 0;
	int count2 = 0;
	JButton button1;
	JButton button2;
	JLabel  label1;
	JLabel  label2;

	/*  
	 * Sometimes it is cleaner to factor the code into instructions for
	 * making components, containers, and listeners and instructions 
	 * for layout. 
	 */
	
	
	TwoButtonPanel(){
		makeComponents();
		makeLayout();
	}

	private void makeComponents(){

		button1 = new JButton("button 1 (press me)");
		button1.addActionListener( this );

		button2 = new JButton("button 2 (press me)");
		button2.addActionListener( this );

		//  label1 and label1 will label fields saying how many presses 
		//  there were for the two buttons.
		
		label1 = new JLabel();
		label1.setFont(new Font("Times", Font.BOLD, 16));
		label1.setBackground(Color.lightGray);
		label1.setOpaque(true);
		label1.setHorizontalAlignment( SwingConstants.CENTER );

		label2 = new JLabel();
		label2.setFont(new Font("Times", Font.BOLD, 16));
		label2.setBackground(new Color(160, 160, 160));
		label2.setOpaque(true);
		label2.setHorizontalAlignment( SwingConstants.CENTER );
	}

	private void makeLayout(){
		setLayout( new GridLayout(2,2));
		add(button1);
		add(label1);	
		add(button2);
		add(label2); 
	}

	public void actionPerformed(ActionEvent e) { 
		if (e.getSource() == button1){
			count1++;
			label1.setText(" pushes: " + count1);
		}
		else if (e.getSource() == button2){
			count2++;
			label2.setText(" pushes " + count2);
		}
	}
}

