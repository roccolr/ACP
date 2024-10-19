package pubsub;

import javax.jms.*;


public class MyListener implements MessageListener {

    @Override
    public void onMessage(Message msg){
        TextMessage text = (TextMessage)msg;
        try{
            String message = text.getText();
            System.out.println("[MYLISTENER]\tricevuto messaggio: "+message+" con proprietà int: "+text.getIntProperty("propInt"));
        }catch(JMSException e){
            e.printStackTrace();
        }
    }
}
