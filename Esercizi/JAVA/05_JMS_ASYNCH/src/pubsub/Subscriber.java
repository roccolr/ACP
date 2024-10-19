package pubsub;

import java.util.Hashtable;

import javax.jms.*;
import javax.naming.*;

public class Subscriber {
    public static void main(String argv[]){
        Hashtable <String,String> prop = new Hashtable<>();
        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        prop.put("topic.soccer", "soccernews");
        prop.put("topic.tennis", "tennisnews");

        try{
            Context jndiContext = new InitialContext(prop);
            TopicConnectionFactory tcf = (TopicConnectionFactory)jndiContext.lookup("TopicConnectionFactory");
            // Topic soccerTopic = (Topic)jndiContext.lookup("soccer");
            Topic tennisTopic = (Topic)jndiContext.lookup("tennis");

            //ho ottenuto gli administered objects. A questo punto ottengo una connesisone
            TopicConnection conn = tcf.createTopicConnection();
            TopicSession session = conn.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
            
            TopicSubscriber sub = session.createSubscriber(tennisTopic);
            sub.setMessageListener(new MyListener());
            conn.start();

            System.out.println("Listener set...");
        }catch(NamingException e){
            e.printStackTrace();
        }catch(JMSException e){
            e.printStackTrace();
        }
    }
}
