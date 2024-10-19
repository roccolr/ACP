package dispatcher;
import javax.jms.*;

public class DispatcherThread extends Thread{
    private boolean preleva;
    private Queue risposta;
    private QueueSession session;
    private ServerProxy proxy;
    private int value;

    public DispatcherThread(boolean preleva, Queue risposta, QueueSession session, ServerProxy proxy, int value){
        this.preleva = preleva;
        this.risposta = risposta;
        this.session = session;
        this.proxy = proxy;
        this.value = value;
    }
    public void run(){
        try{
            if(!preleva){
                proxy.deposita(value);
                QueueSender sender = session.createSender(risposta);
                TextMessage msg = session.createTextMessage();
                msg.setText("deposited");
                sender.send(msg);
                System.out.println("[DISPATCHER]\tinviato messaggio deposited");
            }
            else{
                QueueSender sender = session.createSender(risposta);
                TextMessage msg = session.createTextMessage();
                int res= proxy.preleva();
                msg.setText(Integer.toString(res));
                sender.send(msg);
                System.out.println("[DISPATCHER]\tinviato valore: "+res);

            }

        }catch(JMSException e){
            e.printStackTrace();
        }
    }
}
