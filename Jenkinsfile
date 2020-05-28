node{
    def app
        stage('Cloning Repository') {
            checkout scm
        }
        stage('Testing Code')
        {
                sh 'python3 test.py'  
        }
        stage('Containerizing')
        {
                app = docker.build("ankitpd/project_approval_system")
        }
        stage('Pushing Image')
      {
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
      }
    //stage('Stopping Old Version')
    //{
        //def jobname = "deploy_pas"
        //def job = Jenkins.instance.getItemByFullName(jobname)
            //for (build in job.builds) {
                //if (build.getNumber().toInteger()){
                    //if (build.isBuilding()){
                        //build.doStop();
                        //build.doKill();
                    //}
                //}
            //}
    //}
    stage('Deploying New Version')
    {
        def job = Jenkins.instance.getItemByFullName('deploy_pas')
        job.currentBuild.result = 'ABORTED'
        build job: 'deploy_pas'
    }
}
