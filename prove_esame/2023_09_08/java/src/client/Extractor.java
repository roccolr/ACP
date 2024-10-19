package client;
import java.util.Hashtable;

import javax.jms.*;
import javax.jms.Topic;
import javax.naming.*;


public class Extractor {
    public static void main(String argv[]){
        Hashtable <String, String> prop = new Hashtable<>();

        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        prop.put("topic.temp", "tempTopic");
        prop.put("topic.press", "pressTopic");
        prop.put("topic.data", "dataTopic");

        try{
            Context jndiContext = new InitialContext(prop);

            TopicConnectionFactory topicConnectionFactory = (TopicConnectionFactory)jndiContext.lookup("TopicConnectionFactory");
            Topic data = (Topic)jndiContext.lookup("data");
            Topic press = (Topic)jndiContext.lookup("press");
            Topic temp = (Topic)jndiContext.lookup("temp");

            TopicConnection conn = topicConnectionFactory.createTopicConnection();

            conn.start();

            TopicSession session = conn.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);

            TopicSubscriber dataSubscriber = session.createSubscriber(data);

            dataSubscriber.setMessageListener(new ExtractorListener(temp, press, conn, session));

            while(true){
                Thread.sleep(1000);
            }

        }catch(NamingException e){
            e.printStackTrace();
        }catch(JMSException e){
            e.printStackTrace();
        }catch(InterruptedException e){
            e.printStackTrace();
        }
        
    }
}
