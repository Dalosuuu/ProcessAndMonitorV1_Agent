# What is this project about (draft)?

Endpoint Detection & Response project/software, heavily inspired in Falcon Insight's Crowdstrike's Intelligent EDR Solution 


# Sources:
https://www.crowdstrike.com/wp-content/uploads/2022/03/crowdstrike-falcon-insight-data-sheet.pdf
  Crowdstrike Falcon Insights (Datasheet) - ~/Downloads/crowdstrike-falcon-insight-data-sheet.pdf
https://technology-signals.com/wp-content/uploads/download-manager-files/CrowdStrike_EDR_Whitepaper__1_.pdf  
  Crowdstrike EDR WHITEPAPER - ~/Downloads/CrowdStrike_EDR_Whitepaper__1_.pdf
https://helpcenter.threatq.com/assets/PDFs/Integrations/CrowdStrike_Falcon_Insight_EDR_Operation_Guide_v1.2.0.pdf
  Falcon User Guide -  ~/Downloads/CrowdStrike_Falcon_Insight_EDR_Operation_Guide_v1.2.0.pdf
https://github.com/CrowdStrike/helpful-links
  Github with urls
 


INTELLIGENT EDR
  AUTOMATICALLY UNCOVERS STEALTHY ATTACKERS
     Pairing full endpoint visibility with indicators of attack (IOAs),
     Falcon Insight  behavioral analytics allows it to analyze billions
     of events in real time and to  automatically detect traces of
     suspicious behavior.  IOAs automate and accelerate the detection of
     attacker behaviors and pinpoint attacker activities that
     would otherwise go unnoticed. Thanks to IOAs, it’s no longer necessary
     for security teams to figure out what to look for and then build their
     own searches. 


KERNEL LEVEL ALLOWS CWD FALCON:
  security-related events, such as process creation,
  drivers loading, registry modifications, disk access,
  memory access,  or network connections.

  - Does it needs access in order to see memory access and registry modifications
  or is it something else?

  Extra context:
         This gives security teams a great deal of useful information,
         including local and external addresses to which the  host is connected;
(Nice F) all the user accounts that have logged in, both directly and remotely;
         a summary of changes to ASP keys, executables  and administrative tool usage;
         process executions;
         both summary  and detailed process-level network activity, including DNS requests,  connections, and open ports;
         archive file creation, including RAR and ZIPS;
         and even removable media usage. 

GRAPH DATABASE
  IS GRAPH DATABASE REALLY NEEDED FOR ANALYSIS?
    The information gathered is stored in the CrowdStrike cloud via the  Falcon platform, with architecture based on a situational model. The  model keeps track of all the relationships and contacts between every  endpoint event using a massive, powerful graph database, which  provides details and context rapidly and at scale, for both historical  and real-time data. This enables security teams to quickly investigate  incidents. 
  See WhitePaper Page 12 - Talks about Crowdstrike Threat Graph (Graph Databse)
